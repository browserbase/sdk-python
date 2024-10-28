import time

from playwright.sync_api import Page, Playwright, sync_playwright

from examples import (
    BROWSERBASE_API_KEY,
    BROWSERBASE_PROJECT_ID,
    bb,
)

GRACEFUL_SHUTDOWN_TIMEOUT = 30000  # Assuming 30 seconds, adjust as needed


def check_proxy_bytes(session_id: str) -> None:
    bb.sessions.update(
        id=session_id, project_id=BROWSERBASE_PROJECT_ID, status="REQUEST_RELEASE"
    )
    time.sleep(GRACEFUL_SHUTDOWN_TIMEOUT / 1000)
    updated_session = bb.sessions.retrieve(id=session_id)
    assert (
        updated_session.proxy_bytes is not None and updated_session.proxy_bytes > 0
    ), f"Proxy bytes: {updated_session.proxy_bytes}"


def run_enable_via_create_session(playwright: Playwright) -> None:
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID, proxies=True)

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]
    page.goto("https://www.google.com")
    page_title = page.title()

    page.close()
    browser.close()

    assert page_title == "Google"
    check_proxy_bytes(session.id)


def run_enable_via_querystring_with_created_session(playwright: Playwright) -> None:
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID, proxies=True)

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]
    page.goto("https://www.google.com/")
    page_title = page.title()

    page.close()
    browser.close()

    assert page_title == "Google"
    check_proxy_bytes(session.id)


def extract_from_table(page: Page, cell: str) -> str:
    page.goto("https://www.showmyip.com/")
    page.wait_for_selector("table.iptab")

    td = page.locator(f"table.iptab tr:has-text('{cell}') td:last-child")

    text = td.text_content()
    if not text:
        raise Exception(f"Failed to extract {cell}")
    return text.strip()


def run_geolocation_country(playwright: Playwright) -> None:
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        proxies=[
            {
                "geolocation": {"country": "CA"},
                "type": "browserbase",
            }
        ],
    )

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]

    country = extract_from_table(page, "Country")

    page.close()
    browser.close()

    assert country == "Canada"


def run_geolocation_state(playwright: Playwright) -> None:
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        proxies=[
            {
                "geolocation": {
                    "country": "US",
                    "state": "NY",
                },
                "type": "browserbase",
            }
        ],
    )

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]

    state = extract_from_table(page, "Region")

    page.close()
    browser.close()

    assert state == "New York"


def run_geolocation_american_city(playwright: Playwright) -> None:
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        proxies=[
            {
                "geolocation": {
                    "city": "Los Angeles",
                    "country": "US",
                    "state": "CA",
                },
                "type": "browserbase",
            }
        ],
    )

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]

    city = extract_from_table(page, "City")

    page.close()
    browser.close()

    assert city == "Los Angeles"


def run_geolocation_non_american_city(playwright: Playwright) -> None:
    session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
        proxies=[
            {
                "geolocation": {
                    "city": "London",
                    "country": "GB",
                },
                "type": "browserbase",
            }
        ],
    )

    browser = playwright.chromium.connect_over_cdp(session.connect_url)

    context = browser.contexts[0]
    page = context.pages[0]

    city = extract_from_table(page, "City")

    page.close()
    browser.close()

    assert city == "London"


if __name__ == "__main__":
    with sync_playwright() as playwright:
        # You can run any of these tests by uncommenting them
        run_enable_via_create_session(playwright)
        # run_enable_via_querystring_with_created_session(playwright)
        # run_geolocation_country(playwright)
        # run_geolocation_state(playwright)
        # run_geolocation_american_city(playwright)
        # run_geolocation_non_american_city(playwright)
