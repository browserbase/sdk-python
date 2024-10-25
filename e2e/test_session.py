import os
import re

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, Playwright, expect, sync_playwright

from browserbase import Browserbase

load_dotenv(override=True)
BROWSERBASE_URL = os.environ.get("BROWSERBASE_URL", "wss://connect.browserbase.com")
BROWSERBASE_API_KEY = os.environ.get("BROWSERBASE_API_KEY")
if not BROWSERBASE_API_KEY:
    raise ValueError("BROWSERBASE_API_KEY is not set in environment")
BROWSERBASE_PROJECT_ID = os.environ.get("BROWSERBASE_PROJECT_ID")
if not BROWSERBASE_PROJECT_ID:
    raise ValueError("BROWSERBASE_PROJECT_ID is not set in environment")

bb = Browserbase(api_key=BROWSERBASE_API_KEY)


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p


"""
def test_has_title():

    page = browser.new_page()
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(browser: Browser):
    page = browser.new_page()
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
"""


def test_create_session(playwright: Playwright):
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
    print("Api Key: " + os.environ.get("BROWSERBASE_API_KEY"))
    connect_url = session.connectUrl
    print("connect_url: " + connect_url)
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(
        "wss://connect.browserbase.com?apiKey=" + BROWSERBASE_API_KEY
    )
    context = browser.contexts[0]
    page = context.pages[0]

    page.goto("https://www.google.com")
    page.screenshot(path="screenshot.png")
    print(page.title)
    assert True
