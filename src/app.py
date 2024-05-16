"""Entrypoint file for the affils service.

Set up API routes.
"""

# Built-in libraries:
import os
import subprocess

# Third-party dependencies:
from flask import Flask
from flask import redirect
from flask import render_template

# In-house code:
from . import logger
from .affiliation import Affiliation

app = Flask(__name__)


@app.route("/")
def index():
    """Index route."""
    logger.info("User accessed /")
    return redirect("/affiliations")


@app.route("/affiliations")
def affiliations():
    """The affiliations home page."""
    logger.info("User accessed /affiliations")
    affiliations_set = Affiliation.all()
    return render_template("index.html", affiliations=affiliations_set)


@app.route("/sha")
def current_git_sha():
    """Displays current Git SHA."""
    logger.info("User accessed /sha")
    command = ["git", "rev-parse", "HEAD"]
    output = subprocess.run(command, check=False, capture_output=True).stdout.decode(
        "utf-8"
    )
    # Strip newline character from the end of the string.
    sha = output[0 : len(output) - 1]
    return sha


@app.route("/env")
def display_env_var():
    """Displays environment variable for testing purposes."""
    logger.info("User accessed /env")
    return os.environ.get("SOME_VAR")
