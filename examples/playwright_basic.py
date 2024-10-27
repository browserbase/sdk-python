from playwright.sync_api import Playwright, sync_playwright

from examples import (
    BROWSERBASE_PROJECT_ID,
    bb,
)


def run(playwright: Playwright) -> None:
    # Create a session on Browserbase
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)

    # Connect to the remote session
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(session.connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    # Execute Playwright actions on the remote browser tab
    page.goto("https://news.ycombinator.com/")
    page_title = page.title()
    assert (
        page_title == "Hacker News"
    ), f"Page title is not 'Hacker News', it is '{page_title}'"
    page.screenshot(path="screenshot.png")

    page.close()
    browser.close()
    print("Done!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
