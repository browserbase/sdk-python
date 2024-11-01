# Migration Guide

The Browserbase v1 Python SDK has been rewritten from the ground up and ships with a ton of new features and better support that we can't wait for you to try. This guide is designed to help you maximize your experience with v1.

We hope this guide is useful to you; if you have any questions don't hesitate to reach out to support@browserbase.com or [create a new issue](https://github.com/browserbase/sdk-python/issues/new).

We've written out specific guidelines on how to migrate each v0 method to v1 below. v1 also adds one-to-one mappings for every API endpoint, so you can incorporate new Browserbase features in your codebase with much less lift.

## Breaking Changes

The v1 SDK is more flexible, easier to use, and has a more consistent API. It is also a lot more modular, meaning the majority of function calls have changed from `browserbase.$thing_$do()` to `browserbase.$thing.$do()`. For example:

```python
# v0 SDK
browserbase.list_sessions()

# v1 SDK
bb.sessions.list()
```

### Deleted Methods

`load`, `load_url`, and `screenshot` have been fully removed in the v1 SDK. You can use the following example instead that encapsulates the same functionality using Playwright.

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
    print(f"Done! View replay at https://browserbase.com/sessions/{session.id}")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
```

For async Playwright (like in Jupyter notebooks or IPython environments), you can import `async_playwright` instead of `sync_playwright`.

## Updates to Common Workflows

### Create Session

This is how you would create a session with the v0 SDK, where `CreateSessionOptions` is a Pydantic object defined [here](https://github.com/browserbase/python-sdk/blob/0a499ba29853f20bb3055d7c81c5f61c24fcd9ec/browserbase/__init__.py#L52).

```python
# v0 SDK
from browserbase import Browserbase, CreateSessionOptions

browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)
options = CreateSessionOptions(extensionId='123')
browserbase.create_session(options)
```

Now, you can create a session with the v1 SDK by calling the `create` method on `sessions`.

```python
# v1 SDK
from browserbase import Browserbase

bb = Browserbase(api_key=BROWSERBASE_API_KEY)
session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID, extension_id="some_extension_id")
```

For more complex session creation, you can import `BrowserSettings` and use Pydantic's `TypeAdapter` to conform JSON spec to the appropriate Pydantic class. You can also import each individual subclass.

```python
# v1 SDK
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

### Get Connect URL

In the v0 SDK, you could run `browserbase.get_connect_url()` to create a new session and retrieve its connect url, or `browserbase.get_connect_url(session_id=some_session.id)` to retrieve the connect url for an existing session.

In the v1 SDK, you can create a session and retrieve its connect url in a single call with `bb.sessions.create()`.

```python
# v0 SDK
from browserbase import Browserbase

browserbase = Browserbase(api_key=BROWSERBASE_API_KEY, project_id=BROWSERBASE_PROJECT_ID)

# To create a new session and connect to it
connect_url = browserbase.get_connect_url()

# To connect to an existing session
connect_url = browserbase.get_connect_url(session_id=some_session.id)
```

```python
# v1 SDK
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

### Complete Session

v0 allowed you to complete a session by calling `browserbase.complete_session(session_id=some_session.id)`.

```python
# v0 SDK
browserbase.complete_session(session_id=some_session.id)
```

In the v1 SDK, completing a session is done by updating its status to `REQUEST_RELEASE`.

```python
# v1 SDK
bb.sessions.update(id=session_id, status="REQUEST_RELEASE")
```

## Reference for other methods

These methods have been rewritten for modularity and flexibility. As mentioned above, the pattern here is that the method has been renamed from `browserbase.$thing_$do()` to `bb.$thing.$do()`.

### List Sessions

```python
# v0 SDK
sessions = browserbase.list_sessions()
```

```python
# v1 SDK
sessions = bb.sessions.list()
```

### Get Session

```python
# v0 SDK
session = browserbase.get_session(session_id="some_session_id")
```

```python
# v1 SDK
session = bb.sessions.retrieve(id="some_session_id")
```

### Get Session Recording

```python
# v0 SDK
recording = browserbase.get_session_recording(session_id=some_session.id)
```

```python
# v1 SDK
recording = bb.sessions.recording.retrieve(id="some_session_id")
```

### Get Session Downloads

**Note:** The parameter `retry_interval` is no longer supported. You can configure retries with the following syntax on bb init:

```python
bb = Browserbase(api_key=BROWSERBASE_API_KEY, max_retries=5)
```

Keep in mind, however, that this only affects the default retry behavior, which will only retry on 4xx/5xx errors. The remaining pattern still applies:

```python
# v0 SDK
downloads = browserbase.get_session_downloads(session_id=some_session.id)
```

```python
# v1 SDK
downloads = bb.sessions.downloads.retrieve(id="some_session_id")
```

### Get Debug Connection URLs

```python
# v0 SDK
debug_urls = browserbase.get_debug_connection_urls(session_id=some_session.id)
```

```python
# v1 SDK
debug_urls = bb.sessions.debug.list(id="some_session_id")
```

### Get Session Logs

```python
# v0 SDK
logs = browserbase.get_session_logs(session_id=some_session.id)
```

```python
# v1 SDK
logs = bb.sessions.logs.list(id="some_session_id")
```
