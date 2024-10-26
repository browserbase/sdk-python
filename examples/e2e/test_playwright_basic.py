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


def test_playwright_basic(playwright: Playwright):
    playwright_basic.run(playwright)
