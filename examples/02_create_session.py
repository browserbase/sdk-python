import os
from pprint import pprint

from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright

from browserbase import Browserbase

load_dotenv(override=True)
BROWSERBASE_API_KEY = os.environ["BROWSERBASE_API_KEY"]
BROWSERBASE_PROJECT_ID = os.environ["BROWSERBASE_PROJECT_ID"]


bb = Browserbase(
    api_key=BROWSERBASE_API_KEY
)  # can be omitted if in environment variable

session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
pprint({"session": session})


def run(playwright: Playwright):
    print("Api Key: " + os.environ["BROWSERBASE_API_KEY"])
    connect_url = session.connectUrl
    print("connect_url: " + connect_url)
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    page.goto("https://www.google.com")
    page.screenshot(path="screenshot.png")
    print(page.title)


with sync_playwright() as playwright:
    run(playwright)

update_session_resp = bb.sessions.update(
    id=session.id, status="REQUEST_RELEASE", project_id=BROWSERBASE_PROJECT_ID
)
pprint({"update_session_resp": update_session_resp})

print("done")
