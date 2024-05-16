"""Initialize stuff."""

# Built-in dependencies:
import logging

# Third-party dependencies:
from dotenv import load_dotenv

# Make sure environment variables are present.
load_dotenv()

# Configure logger.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
