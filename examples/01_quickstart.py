import os

from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

load_dotenv(override=True)
BROWSERBASE_API_KEY = os.environ["BROWSERBASE_API_KEY"]
BROWSERBASE_PROJECT_ID = os.environ["BROWSERBASE_PROJECT_ID"]


def run(playwright: Playwright):
    print("Api Key: " + os.environ["BROWSERBASE_API_KEY"])
    connect_url = "wss://connect.browserbase.com?apiKey=" + BROWSERBASE_API_KEY
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


with sync_playwright() as playwright:
    run(playwright)
