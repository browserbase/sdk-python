from typing import Dict

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from examples import BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, bb


class BrowserbaseConnection(RemoteConnection):
    """
    Manage a single session with Browserbase.
    """

    session_id: str

    def __init__(self, session_id: str, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)  # type: ignore
        self.session_id = session_id

    def get_remote_connection_headers(  # type: ignore
        self, parsed_url: str, keep_alive: bool = False
    ) -> Dict[str, str]:
        headers = super().get_remote_connection_headers(parsed_url, keep_alive)  # type: ignore

        # Update headers to include the Browserbase required information
        headers["x-bb-api-key"] = BROWSERBASE_API_KEY
        headers["session-id"] = self.session_id

        return headers  # type: ignore


def run() -> None:
    # Use the custom class to create and connect to a new browser session
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
    connection = BrowserbaseConnection(session.id, session.selenium_remote_url)
    driver = webdriver.Remote(
        command_executor=connection, options=webdriver.ChromeOptions()  # type: ignore
    )

    # Print a bit of info about the browser we've connected to
    print(
        "Connected to Browserbase",
        f"{driver.name} version {driver.caps['browserVersion']}",  # type: ignore
    )

    try:
        # Perform our browser commands
        driver.get("https://www.sfmoma.org")
        print(f"At URL: {driver.current_url} | Title: {driver.title}")
        assert driver.current_url == "https://www.sfmoma.org/"
        assert driver.title == "SFMOMA"

    finally:
        # Make sure to quit the driver so your session is ended!
        driver.quit()


if __name__ == "__main__":
    run()
