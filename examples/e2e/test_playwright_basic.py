import pytest
from playwright.sync_api import Playwright, sync_playwright

from browserbase import Browserbase

from .. import (
    BROWSERBASE_API_KEY,
    playwright_basic,
)

bb = Browserbase(api_key=BROWSERBASE_API_KEY)


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


def test_create_session(playwright: Playwright):
    page = playwright_basic.run(playwright)
    assert page["title"] == "Hacker News"
