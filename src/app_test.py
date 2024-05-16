"""Test code in the entrypoint file for the affils service."""

# In-house code:
from .app import app

# Configure app for testing.
app.config.update({"TESTING": True})

# Constants:
CLIENT = app.test_client()


def test_index_route():
    """Ensure index route redirects."""
    response = CLIENT.get("/")
    assert response.status_code == 302


def test_affiliations_route():
    """Ensure index route redirects."""
    response = CLIENT.get("/affiliations")
    assert response.status_code == 200
    assert "<table>" in response.text
    assert "<th>ID</th>" in response.text
    assert "<td>10000</td>" in response.text
    assert "<th>Name</th>" in response.text
    assert "<td>Interface Admin</td>" in response.text


def test_sha_route():
    """Ensure we can get a SHA."""
    response = CLIENT.get("/sha")
    assert response.status_code == 200
    assert len(response.text) == 40  # SHA-1 is 40 characters in length.
