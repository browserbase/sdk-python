# V1 Migration Guide

The Browserbase v1 Python SDK has been rewritten from the ground up and ships with a ton of new features and better support that we can't wait for you to try. This guide is designed to help you maximize your experience with V1.

We hope this guide is useful to you; if you have any questions don't hesitate to reach out to support@browserbase.com or [create a new issue](https://github.com/browserbase/sdk-python/issues/new).

We've also rewritten our old SDK functionalities to use the new SDK with analogous function signatures below.

## Major Changes

V1 SDK is a complete rewrite of the old SDK. The new SDK is more flexible, easier to use, and has a more consistent API. It is also a lot more modular. The majority of the syntax changes are as follows:

```python
# Old SDK
browserbase.list_sessions()

# New SDK
bb.sessions.list()
```

### Creating a Session

Similar to the above, the new way to create a session is to use the `create` method on the `sessions` object. However, the `CreateSessionOptions` object is now broken up into several params, saving you from having to import and instantiate a Pydantic object. For more on this, see [below](#create-session).

## Deprecated Methods

`load`, `load_url`, and `screenshot` are fully deprecated. You can use the following example instead that encapsulates the same functionality using Playwright.

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

For async Playwright, you can import `async_playwright` instead.

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
from pydantic import TypeAdapter

bb = Browserbase(api_key=BROWSERBASE_API_KEY)
session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID, extension_id="some_extension_id")
```

For more complex session creation, you can import `BrowserSettings` and use Pydantic's `TypeAdapter` to conform JSON spec to the appropriate Pydantic class. You can also import each individual subclass, but this may be rather tedious.

```python
from browserbase import Browserbase
from pydantic import TypeAdapter
from browserbase.types.session_create_params import BrowserSettings

session = bb.sessions.create(
        project_id=BROWSERBASE_PROJECT_ID,
		extension_id="some_extension_id",
        browser_settings=TypeAdapter(BrowserSettings).validate_python(
            {"context": {"id": context_id, "persist": True}}
        ),
    )
```

## Get Connect Url

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

def get_connect_url(bb: Browserbase, session_id: str = None):
	"""
	Retrieve a connect url for a given session or create a new one.

	If a session id is provided, retrieve the connect url for the existing session.
	Otherwise, create a new session and return the connect url.
	"""
	if session_id:
		session = bb.sessions.retrieve(id=session_id)
	else:
		session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
	return session.connect_url

connect_url = get_connect_url(bb, session_id="some_session_id")
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

def list_sessions(bb: Browserbase):
	"""
	List all sessions for the given project.
	"""
	return bb.sessions.list()

sessions = list_sessions(bb)
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

def complete_session(bb: Browserbase, session_id: str):
	"""
	Complete a session by updating its status to REQUEST_RELEASE.
	"""
	bb.sessions.update(id=session_id, status="REQUEST_RELEASE")

complete_session(bb, session_id="some_session_id")
```

## Get Session

### Old SDK

```python
from browserbase import Browserbase
browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
session = browserbase.get_session(session_id="some_session_id")
```

### New SDK

```python
from browserbase import Browserbase
bb = Browserbase(api_key=BROWSERBASE_API_KEY)

def get_session(bb: Browserbase, session_id: str):
	"""
	Retrieve a session by id.
	"""
	return bb.sessions.retrieve(id=session_id)

session = get_session(bb, session_id="some_session_id")
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
def get_session_recording(bb: Browserbase, session_id: str):
	"""
	Retrieve a session recording by id.
	"""
	return bb.sessions.recording.retrieve(id=session_id)

recording = get_session_recording(bb, session_id="some_session_id")
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

def get_session_downloads(bb: Browserbase, session_id: str):
	"""
	Retrieve a session's downloads by id.
	"""
	return bb.sessions.downloads.list(id=session_id)

downloads = get_session_downloads(bb, session_id="some_session_id")
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

def get_debug_connection_urls(bb: Browserbase, session_id: str):
	"""
	Retrieve a session's debug connection urls by id.
	"""
	return bb.sessions.debug(id=session_id)

debug_urls = get_debug_connection_urls(bb, session_id="some_session_id")
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

def get_session_logs(bb: Browserbase, session_id: str):
	"""
	Retrieve a session's logs by id.
	"""
	return bb.sessions.logs.list(id=session_id)

logs = get_session_logs(bb, session_id="some_session_id")
```
