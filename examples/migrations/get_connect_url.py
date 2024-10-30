from browserbase import Browserbase

# import os
from typing import Optional

# BROWSERBASE_API_KEY = os.environ.get("BROWSERBASE_API_KEY")
# BROWSERBASE_PROJECT_ID = os.environ.get("BROWSERBASE_PROJECT_ID")
# bb = Browserbase(api_key=BROWSERBASE_API_KEY)


def get_connect_url(
    bb: Browserbase, session_id: Optional[str] = None, proxy: Optional[bool] = None
):
    base_url = f"{BROWSERBASE_CONNECT_URL}?apiKey={bb.api_key}"
    if session_id:
        base_url += f"&sessionId={session_id}"
    if proxy:
        base_url += "&enableProxy=true"

    return base_url


def list_sessions(bb: Browserbase):
    return bb.sessions.list()


# Original Signature: def create_session(self, options: Optional[CreateSessionOptions] = None) -> Session
# New Signature: https://github.com/browserbase/sdk-python/blob/548e0314002e2e9a8c1ab78b54b20bb6e7dea769/src/browserbase/resources/sessions/sessions.py#L101-L117
def create_session(bb: Browserbase, project_id: str, **kwargs):
    return bb.sessions.create(project_id=project_id, **kwargs)


def complete_session(bb: Browserbase, project_id: str, session_id: str):
    return bb.sessions.update(
        id=session_id, project_id=project_id, status="REQUEST_RELEASE"
    )


def get_session(bb: Browserbase, session_id: str):
    return bb.sessions.retrieve(id=session_id)


def get_session_recording(bb: Browserbase, session_id: str):
    return bb.sessions.recording.retrieve(id=session_id)


# Original Signature: def get_session_downloads(self, session_id: str, retry_interval: int = 2000, retry_count: int = 2) -> Optional[bytes]:
# To avoid rate limiting, we don't allow retry_interval to be configured; however, you can configure retries with the following syntax on bb init:
# bb = Browserbase(api_key=BROWSERBASE_API_KEY, max_retries=5)
def get_session_downloads(bb: Browserbase, session_id: str):
    return bb.sessions.downloads.list(id=session_id)


def get_debug_connection_urls(bb: Browserbase, session_id: str):
    return bb.sessions.debug(id=session_id)


def get_session_logs(bb: Browserbase, session_id: str):
    return bb.sessions.logs.list(id=session_id)


bb = Browserbase(api_key=BROWSERBASE_API_KEY)
bb.sessions.debug()
