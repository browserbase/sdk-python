from playwright.sync_api import Playwright, ConsoleMessage, sync_playwright

from examples import (
    BROWSERBASE_API_KEY,
    BROWSERBASE_PROJECT_ID,
    BROWSERBASE_CONNECT_URL,
    bb,
)

DEFAULT_CAPTCHA_URL = "https://www.google.com/recaptcha/api2/demo"
OVERRIDE_TIMEOUT = 60000  # 60 seconds, adjust as needed


def run(playwright: Playwright):
    # Create a session on Browserbase
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
    assert session.id is not None
    assert session.status == "RUNNING", f"Session status is {session.status}"

    # Connect to the remote session
    connect_url = (
        f"{BROWSERBASE_CONNECT_URL}?sessionId={session.id}&apiKey={BROWSERBASE_API_KEY}"
    )
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    captcha_solving_started = False
    captcha_solving_finished = False

    # Browserbase logs messages to the console to indicate when captcha solving has started and finished
    # We can track these messages to know when the captcha solving has started and finished
    def handle_console(msg: ConsoleMessage):
        nonlocal captcha_solving_started, captcha_solving_finished
        if msg.text == "browserbase-solving-started":
            captcha_solving_started = True
            page.evaluate("window.captchaSolvingFinished = false;")
        elif msg.text == "browserbase-solving-finished":
            captcha_solving_finished = True
            page.evaluate("window.captchaSolvingFinished = true;")

    page.on("console", handle_console)

    page.goto(DEFAULT_CAPTCHA_URL, wait_until="networkidle")
    page.wait_for_function(
        "() => window.captchaSolvingFinished === true", timeout=OVERRIDE_TIMEOUT
    )

    assert captcha_solving_started, "Captcha solving did not start"
    assert captcha_solving_finished, "Captcha solving did not finish"

    page.close()
    browser.close()
    print("Done!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
