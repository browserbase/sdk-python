import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

from browserbase import Browserbase

from .. import (
    BROWSERBASE_API_KEY,
    playwright_basic,
    playwright_captcha,
    playwright_contexts,
    playwright_downloads,
)

bb = Browserbase(api_key=BROWSERBASE_API_KEY)
load_dotenv()

SKIP_CAPTCHA_SOLVING = os.getenv("SKIP_CAPTCHA_SOLVING", "true").lower() == "true"


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


def test_playwright_basic(playwright: Playwright):
    playwright_basic.run(playwright)


def test_playwright_captcha(playwright: Playwright):
    if SKIP_CAPTCHA_SOLVING:
        pytest.skip("Skipping captcha solving")
    playwright_captcha.run(playwright)


def test_playwright_contexts(playwright: Playwright):
    playwright_contexts.run(playwright)


def test_playwright_downloads(playwright: Playwright):
    playwright_downloads.run(playwright)
