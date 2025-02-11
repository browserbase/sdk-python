import time
from typing import Optional

from pydantic import TypeAdapter
from playwright.sync_api import Cookie, Browser, Playwright, sync_playwright

from examples import BROWSERBASE_PROJECT_ID, bb
from browserbase.types.session_create_params import (
    BrowserSettings,
    BrowserSettingsContext,
)

CONTEXT_TEST_URL = "https://www.browserbase.com"
SECOND = 1000


def add_hour(date: float) -> int:
    return int((date + 3600) * 1000) // SECOND


def find_cookie(browser: Browser, name: str) -> Optional[Cookie]:
    default_context = browser.contexts[0]
    cookies = default_context.cookies()
    return next((cookie for cookie in cookies if cookie.get("name") == name), None)


def run(playwright: Playwright) -> None:
    context_id = None
    session_id = None
    test_cookie_name = None
    test_cookie_value = None

    # Step 1: Creates a context
    context = bb.contexts.create(project_id=BROWSERBASE_PROJECT_ID)
    assert context.id is not None
    context_id = context.id

    uploaded_context = bb.contexts.retrieve(id=context_id)
    assert uploaded_context.id == context_id

    # Step 2: Creates a session with the context
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        browser_settings=TypeAdapter(BrowserSettings).validate_python({"context": {"id": context_id, "persist": True}}),
    )
    print(session)

    assert session.context_id == context_id, f"Session context_id is {session.context_id}, expected {context_id}"
    session_id = session.id

    # Step 3: Populates and persists the context
    print(f"Populating context {context_id} during session {session_id}")
    connect_url = session.connect_url
    browser = playwright.chromium.connect_over_cdp(connect_url)
    page = browser.contexts[0].pages[0]

    page.goto(CONTEXT_TEST_URL, wait_until="domcontentloaded")

    now = time.time()
    test_cookie_name = f"bb_{int(now * 1000)}"
    test_cookie_value = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime(now))
    browser.contexts[0].add_cookies(
        [
            {
                "domain": ".browserbase.com",
                "expires": add_hour(now),
                "name": test_cookie_name,
                "path": "/",
                "value": test_cookie_value,
            }
        ]
    )

    assert find_cookie(browser, test_cookie_name) is not None

    page.goto("https://www.google.com", wait_until="domcontentloaded")
    page.go_back()

    assert find_cookie(browser, test_cookie_name) is not None

    page.close()
    browser.close()

    time.sleep(5)

    # Step 4: Creates another session with the same context
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        browser_settings=BrowserSettings(context=BrowserSettingsContext(id=context_id, persist=True)),
    )
    assert session.context_id == context_id, f"Session context_id is {session.context_id}, expected {context_id}"
    session_id = session.id

    # Step 5: Uses context to find previous state
    print(f"Reusing context {context_id} during session {session_id}")
    connect_url = session.connect_url
    browser = playwright.chromium.connect_over_cdp(connect_url)
    page = browser.contexts[0].pages[0]

    page.goto(CONTEXT_TEST_URL, wait_until="domcontentloaded")

    found_cookie = find_cookie(browser, test_cookie_name)
    print(found_cookie)
    assert found_cookie is not None
    assert found_cookie.get("value") == test_cookie_value

    page.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
