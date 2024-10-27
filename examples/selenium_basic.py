from examples import bb, BROWSERBASE_PROJECT_ID, BROWSERBASE_API_KEY
from browserbase.types import SessionCreateResponse
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.remote_connection import RemoteConnection


class BrowserbaseConnection(RemoteConnection):
    """
    Manage a single session with Browserbase.
    """

    browserbase_session: SessionCreateResponse

    def __init__(self, *args, **kwargs):
        self.browserbase_session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
        super().__init__(*args, **kwargs)

    def get_remote_connection_headers(self, parsed_url, keep_alive=False):
        headers = super().get_remote_connection_headers(parsed_url, keep_alive)

        # Update headers to include the Browserbase required information
        headers["x-bb-api-key"] = BROWSERBASE_API_KEY
        headers["session-id"] = self.browserbase_session.id

        return headers


def run(driver: WebDriver):
    # Instruct the browser to go to the SF MOMA page
    driver.get("https://www.sfmoma.org")

    # Print out a bit of info about the page it landed on
    print(f"{driver.current_url=} | {driver.title=}")

    ...


# Use the custom class to create and connect to a new browser session
connection = BrowserbaseConnection("http://connect.browserbase.com/webdriver")
driver = webdriver.Remote(connection, options=webdriver.ChromeOptions())

# Print a bit of info about the browser we've connected to
print(
    "Connected to Browserbase",
    f"{driver.name} version {driver.caps['browserVersion']}",
)

try:
    # Perform our browser commands
    run(driver)

finally:
    # Make sure to quit the driver so your session is ended!
    driver.quit()
