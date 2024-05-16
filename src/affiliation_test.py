"""Test the affiliations module."""

# In-house code:
from .affiliation import Affiliation


def test_all():
    """Test the all method."""
    # This test assumes you have greater than 1 affiliation in your DB.
    all_affiliations = Affiliation.all()
    assert len(all_affiliations) > 1
