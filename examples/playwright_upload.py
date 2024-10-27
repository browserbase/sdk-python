from pathlib import Path

from playwright.sync_api import Playwright, sync_playwright

from examples import (
    BROWSERBASE_API_KEY,
    BROWSERBASE_PROJECT_ID,
    BROWSERBASE_CONNECT_URL,
    bb,
)

PATH_TO_UPLOAD = Path.cwd() / "examples" / "packages" / "logo.png"


def run(playwright: Playwright) -> None:
    # Create a session
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)

    # Construct the URL
    url = (
        f"{BROWSERBASE_CONNECT_URL}?apiKey={BROWSERBASE_API_KEY}&sessionId={session.id}"
    )

    # Connect to the browser
    browser = playwright.chromium.connect_over_cdp(url)
    context = browser.contexts[0]
    page = context.pages[0]

    try:
        # Navigate to the upload test page
        page.goto("https://browser-tests-alpha.vercel.app/api/upload-test")

        # Locate the file input element
        file_input = page.locator("#fileUpload")
        file_input.set_input_files(str(PATH_TO_UPLOAD))

        # Get the uploaded file name
        file_name_span = page.locator("#fileName")
        file_name = file_name_span.inner_text()

        # Get the uploaded file size
        file_size_span = page.locator("#fileSize")
        file_size = int(file_size_span.inner_text())

        # Assert the file name and size
        assert (
            file_name == "logo.png"
        ), f"Expected file name to be 'logo.png', but got '{file_name}'"
        assert (
            file_size > 0
        ), f"Expected file size to be greater than 0, but got {file_size}"

        print("File upload test passed successfully!")

    finally:
        # Clean up
        page.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
