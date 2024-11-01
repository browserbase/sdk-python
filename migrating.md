# Upgrade guide to v1.0

The Browserbase v1.0.0 Python SDK has been rewritten from the ground up and ships with a ton of new features and better support that we can't wait for you to try. Unfortunately, however, this means that the old SDKs will be deprecated and archived in favor of the new SDK.

We hope this guide is useful to you; if you have any questions don't hesitate to reach out to support@browserbase.com or [create a new issue](https://github.com/browserbase/sdk-python/issues/new).

## Create Session

### Old SDK

```python
from browserbase import Browserbase, CreateSessionOptions

browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
options = CreateSessionOptions(extensionId='123')
browserbase.create_session(options)
```

Function signature: `def create_session(self, options: Optional[CreateSessionOptions] = None)`

`CreateSessionOptions` is a Pydantic object defined [here](https://github.com/browserbase/python-sdk/blob/0a499ba29853f20bb3055d7c81c5f61c24fcd9ec/browserbase/__init__.py#L52) in the old SDK.

### New SDK

```python
from browserbase import Browserbase

bb = Browserbase(api_key=BROWSERBASE_API_KEY)
session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
```

For more complex session creation, you can import `BrowserSettings` and use Pydantic's `TypeAdapter` to conform JSON spec to the appropriate Pydantic class. You can also import each individual subclass, but this may be rather tedious.

```python
from browserbase import Browserbase
from pydantic import TypeAdapter
from browserbase.types.session_create_params import BrowserSettings

session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
		extension_id="some_extension_id"
        browser_settings=TypeAdapter(BrowserSettings).validate_python(
            {"context": {"id": context_id, "persist": True}}
        ),
    )
```

## Get Connection Url

### Old SDK

```python
from browserbase import Browserbase

browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)

# To create a new session and connect to it
connect_url = browserbase.get_connect_url()

# To connect to a created session
connect_url = browserbase.get_connect_url(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)

# We must create a session first
session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
connect_url = session.connect_url
```

## List Sessions

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
sessions = browserbase.list_sessions()
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
sessions = bb.sessions.list()
```

## Complete Session

### Old SDK

```python
from browserbase import Browserbase

browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
browserbase.complete_session(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
bb.sessions.update(id=some_session.id, status="REQUEST_RELEASE")
```

## Get Session

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
session = browserbase.get_session(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
session = bb.sessions.retrieve(id=some_session.id)
```

## Get Session Recording

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
recording = browserbase.get_session_recording(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
recording = bb.sessions.recording.retrieve(id=some_session.id)
```

## Get Session Downloads

### Old SDK

> [!NOTE]  
> The parameter `retry_interval` is no longer supported. You can configure retries with the following syntax on bb init:
>
> `bb = Browserbase(api_key=BROWSERBASE_API_KEY, max_retries=5)`

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
downloads = browserbase.get_session_downloads(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
downloads = bb.sessions.downloads.list(id=some_session.id)
```

## Get Debug Connection URLs

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
debug_urls = browserbase.get_debug_connection_urls(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
debug_urls = bb.sessions.debug(id=some_session.id)
```

## Get Session Logs

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
logs = browserbase.get_session_logs(session_id=some_session.id)
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)
logs = bb.sessions.logs.list(id=some_session.id)
```

# Deprecated Methods

`load`, `load_url`, and `screenshot` are fully deprecated. You can use the following example instead that encapsulates the same functionality using Playwright

```python
from playwright.sync_api import Playwright, sync_playwright
from browserbase import Browserbase

bb = Browserbase(api_key=BROWSERBASE_API_KEY)

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
```
