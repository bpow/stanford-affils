"""Allows users to log in."""

# Built-in libraries:
import base64
import hashlib
import hmac
import os

# Third-party dependencies:
import boto3
from flask import session

# In-house code:
from . import logger

client = boto3.client(
    "cognito-idp",
    aws_access_key_id=os.environ.get("AFFILS_AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AFFILS_AWS_SECRET_KEY"),
    region_name=os.environ.get("AFFILS_AWS_REGION"),
)


class User:
    """Define the members and methods of an affils user."""

    # pylint: disable=too-few-public-methods

    def __init__(self, email: str, password: str):
        """Create a new user object."""
        self.email = email
        self.password = password

    def _secret_hash(self):
        """Return secret hash value for authentication.

        When you create a Cognito app, you're given the option to
        generate a client secret that is used to compute a secret hash
        for authentication.

        See:
        https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash
        """
        client_secret_key = os.environ.get("AFFILS_AWS_COGNITO_APP_CLIENT_SECRET")
        username = self.email
        client_id = os.environ.get("AFFILS_AWS_COGNITO_APP_CLIENT_ID")
        message = bytes(username + client_id, "utf-8")
        key = bytes(client_secret_key, "utf-8")
        return base64.b64encode(
            hmac.new(key, message, digestmod=hashlib.sha256).digest()
        ).decode()

    def login(self):
        """Log the user in."""
        try:
            # Try to log the user in.
            response = client.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": self.email,
                    "PASSWORD": self.password,
                    "SECRET_HASH": self._secret_hash(),
                },
                ClientId=os.environ.get("AFFILS_AWS_COGNITO_APP_CLIENT_ID"),
            )
            # Add user's email and authentication result to the session.
            session["email"] = self.email
            session["tokens"] = response["AuthenticationResult"]
        except client.exceptions.NotAuthorizedException as err:
            logger.error(err)
            logger.error("User %s was not authorized", self.email)
