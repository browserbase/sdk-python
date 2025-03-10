# Contexts

Types:

```python
from browserbase.types import Context, ContextCreateResponse, ContextUpdateResponse
```

Methods:

- <code title="post /v1/contexts">client.contexts.<a href="./src/browserbase/resources/contexts.py">create</a>(\*\*<a href="src/browserbase/types/context_create_params.py">params</a>) -> <a href="./src/browserbase/types/context_create_response.py">ContextCreateResponse</a></code>
- <code title="get /v1/contexts/{id}">client.contexts.<a href="./src/browserbase/resources/contexts.py">retrieve</a>(id) -> <a href="./src/browserbase/types/context.py">Context</a></code>
- <code title="put /v1/contexts/{id}">client.contexts.<a href="./src/browserbase/resources/contexts.py">update</a>(id) -> <a href="./src/browserbase/types/context_update_response.py">ContextUpdateResponse</a></code>

# Extensions

Types:

```python
from browserbase.types import Extension
```

Methods:

- <code title="post /v1/extensions">client.extensions.<a href="./src/browserbase/resources/extensions.py">create</a>(\*\*<a href="src/browserbase/types/extension_create_params.py">params</a>) -> <a href="./src/browserbase/types/extension.py">Extension</a></code>
- <code title="get /v1/extensions/{id}">client.extensions.<a href="./src/browserbase/resources/extensions.py">retrieve</a>(id) -> <a href="./src/browserbase/types/extension.py">Extension</a></code>
- <code title="delete /v1/extensions/{id}">client.extensions.<a href="./src/browserbase/resources/extensions.py">delete</a>(id) -> None</code>

# Projects

Types:

```python
from browserbase.types import Project, ProjectUsage, ProjectListResponse
```

Methods:

- <code title="get /v1/projects/{id}">client.projects.<a href="./src/browserbase/resources/projects.py">retrieve</a>(id) -> <a href="./src/browserbase/types/project.py">Project</a></code>
- <code title="get /v1/projects">client.projects.<a href="./src/browserbase/resources/projects.py">list</a>() -> <a href="./src/browserbase/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="get /v1/projects/{id}/usage">client.projects.<a href="./src/browserbase/resources/projects.py">usage</a>(id) -> <a href="./src/browserbase/types/project_usage.py">ProjectUsage</a></code>

# Sessions

Types:

```python
from browserbase.types import (
    Session,
    SessionLiveURLs,
    SessionCreateResponse,
    SessionRetrieveResponse,
    SessionListResponse,
)
```

Methods:

- <code title="post /v1/sessions">client.sessions.<a href="./src/browserbase/resources/sessions/sessions.py">create</a>(\*\*<a href="src/browserbase/types/session_create_params.py">params</a>) -> <a href="./src/browserbase/types/session_create_response.py">SessionCreateResponse</a></code>
- <code title="get /v1/sessions/{id}">client.sessions.<a href="./src/browserbase/resources/sessions/sessions.py">retrieve</a>(id) -> <a href="./src/browserbase/types/session_retrieve_response.py">SessionRetrieveResponse</a></code>
- <code title="post /v1/sessions/{id}">client.sessions.<a href="./src/browserbase/resources/sessions/sessions.py">update</a>(id, \*\*<a href="src/browserbase/types/session_update_params.py">params</a>) -> <a href="./src/browserbase/types/session.py">Session</a></code>
- <code title="get /v1/sessions">client.sessions.<a href="./src/browserbase/resources/sessions/sessions.py">list</a>(\*\*<a href="src/browserbase/types/session_list_params.py">params</a>) -> <a href="./src/browserbase/types/session_list_response.py">SessionListResponse</a></code>
- <code title="get /v1/sessions/{id}/debug">client.sessions.<a href="./src/browserbase/resources/sessions/sessions.py">debug</a>(id) -> <a href="./src/browserbase/types/session_live_urls.py">SessionLiveURLs</a></code>

## Downloads

Methods:

- <code title="get /v1/sessions/{id}/downloads">client.sessions.downloads.<a href="./src/browserbase/resources/sessions/downloads.py">list</a>(id) -> BinaryAPIResponse</code>

## Logs

Types:

```python
from browserbase.types.sessions import SessionLog, LogListResponse
```

Methods:

- <code title="get /v1/sessions/{id}/logs">client.sessions.logs.<a href="./src/browserbase/resources/sessions/logs.py">list</a>(id) -> <a href="./src/browserbase/types/sessions/log_list_response.py">LogListResponse</a></code>

## Recording

Types:

```python
from browserbase.types.sessions import SessionRecording, RecordingRetrieveResponse
```

Methods:

- <code title="get /v1/sessions/{id}/recording">client.sessions.recording.<a href="./src/browserbase/resources/sessions/recording.py">retrieve</a>(id) -> <a href="./src/browserbase/types/sessions/recording_retrieve_response.py">RecordingRetrieveResponse</a></code>

## Uploads

Types:

```python
from browserbase.types.sessions import UploadCreateResponse
```

Methods:

- <code title="post /v1/sessions/{id}/uploads">client.sessions.uploads.<a href="./src/browserbase/resources/sessions/uploads.py">create</a>(id, \*\*<a href="src/browserbase/types/sessions/upload_create_params.py">params</a>) -> <a href="./src/browserbase/types/sessions/upload_create_response.py">UploadCreateResponse</a></code>
