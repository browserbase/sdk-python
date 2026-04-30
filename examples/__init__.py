import os

from dotenv import load_dotenv

from browserbase import Browserbase

# Load our environment variables
load_dotenv(override=True)

# Make sure we have the required environment variables
_BROWSERBASE_API_KEY = os.environ.get("BROWSERBASE_API_KEY")
if not _BROWSERBASE_API_KEY:
    raise ValueError("BROWSERBASE_API_KEY is not set in environment")
BROWSERBASE_API_KEY: str = _BROWSERBASE_API_KEY
_BROWSERBASE_PROJECT_ID = os.environ.get("BROWSERBASE_PROJECT_ID")
if not _BROWSERBASE_PROJECT_ID:
    raise ValueError("BROWSERBASE_PROJECT_ID is not set in environment")
BROWSERBASE_PROJECT_ID = _BROWSERBASE_PROJECT_ID or ""

# Instantiate our Browserbase client
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
