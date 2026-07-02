# Certificates

Types:

```python
from browserbase.types import Certificate, CertificateListResponse
```

Methods:

- <code title="post /v1/certificates">client.certificates.<a href="./src/browserbase/resources/certificates.py">create</a>(\*\*<a href="src/browserbase/types/certificate_create_params.py">params</a>) -> <a href="./src/browserbase/types/certificate.py">Certificate</a></code>
- <code title="get /v1/certificates/{id}">client.certificates.<a href="./src/browserbase/resources/certificates.py">retrieve</a>(id) -> <a href="./src/browserbase/types/certificate.py">Certificate</a></code>
- <code title="get /v1/certificates">client.certificates.<a href="./src/browserbase/resources/certificates.py">list</a>() -> <a href="./src/browserbase/types/certificate_list_response.py">CertificateListResponse</a></code>
- <code title="delete /v1/certificates/{id}">client.certificates.<a href="./src/browserbase/resources/certificates.py">delete</a>(id) -> None</code>

# Contexts

Types:

```python
from browserbase.types import Context, ContextCreateResponse, ContextUpdateResponse
```

Methods:

- <code title="post /v1/contexts">client.contexts.<a href="./src/browserbase/resources/contexts.py">create</a>(\*\*<a href="src/browserbase/types/context_create_params.py">params</a>) -> <a href="./src/browserbase/types/context_create_response.py">ContextCreateResponse</a></code>
- <code title="get /v1/contexts/{id}">client.contexts.<a href="./src/browserbase/resources/contexts.py">retrieve</a>(id) -> <a href="./src/browserbase/types/context.py">Context</a></code>
- <code title="put /v1/contexts/{id}">client.contexts.<a href="./src/browserbase/resources/contexts.py">update</a>(id) -> <a href="./src/browserbase/types/context_update_response.py">ContextUpdateResponse</a></code>
- <code title="delete /v1/contexts/{id}">client.contexts.<a href="./src/browserbase/resources/contexts.py">delete</a>(id) -> None</code>

# Extensions

Types:

```python
from browserbase.types import Extension
```

Methods:

- <code title="post /v1/extensions">client.extensions.<a href="./src/browserbase/resources/extensions.py">create</a>(\*\*<a href="src/browserbase/types/extension_create_params.py">params</a>) -> <a href="./src/browserbase/types/extension.py">Extension</a></code>
- <code title="get /v1/extensions/{id}">client.extensions.<a href="./src/browserbase/resources/extensions.py">retrieve</a>(id) -> <a href="./src/browserbase/types/extension.py">Extension</a></code>
- <code title="delete /v1/extensions/{id}">client.extensions.<a href="./src/browserbase/resources/extensions.py">delete</a>(id) -> None</code>

# FetchAPI

Types:

```python
from browserbase.types import FetchAPICreateResponse
```

Methods:

- <code title="post /v1/fetch">client.fetch_api.<a href="./src/browserbase/resources/fetch_api.py">create</a>(\*\*<a href="src/browserbase/types/fetch_api_create_params.py">params</a>) -> <a href="./src/browserbase/types/fetch_api_create_response.py">FetchAPICreateResponse</a></code>

# Projects

Types:

```python
from browserbase.types import Project, ProjectUsage, ProjectListResponse
```

Methods:

- <code title="get /v1/projects/{id}">client.projects.<a href="./src/browserbase/resources/projects.py">retrieve</a>(id) -> <a href="./src/browserbase/types/project.py">Project</a></code>
- <code title="get /v1/projects">client.projects.<a href="./src/browserbase/resources/projects.py">list</a>() -> <a href="./src/browserbase/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="get /v1/projects/{id}/usage">client.projects.<a href="./src/browserbase/resources/projects.py">usage</a>(id) -> <a href="./src/browserbase/types/project_usage.py">ProjectUsage</a></code>

# Search

Types:

```python
from browserbase.types import SearchWebResponse
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/browserbase/resources/search.py">web</a>(\*\*<a href="src/browserbase/types/search_web_params.py">params</a>) -> <a href="./src/browserbase/types/search_web_response.py">SearchWebResponse</a></code>

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

## Replays

Types:

```python
from browserbase.types.sessions import ReplayRetrieveResponse
```

Methods:

- <code title="get /v1/sessions/{id}/replays">client.sessions.replays.<a href="./src/browserbase/resources/sessions/replays.py">retrieve</a>(id) -> <a href="./src/browserbase/types/sessions/replay_retrieve_response.py">ReplayRetrieveResponse</a></code>
- <code title="get /v1/sessions/{id}/replays/{pageId}">client.sessions.replays.<a href="./src/browserbase/resources/sessions/replays.py">retrieve_page</a>(page_id, \*, id) -> BinaryAPIResponse</code>

# Agents

Types:

```python
from browserbase.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
)
```

Methods:

- <code title="post /v1/agents">client.agents.<a href="./src/browserbase/resources/agents/agents.py">create</a>(\*\*<a href="src/browserbase/types/agent_create_params.py">params</a>) -> <a href="./src/browserbase/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v1/agents/{agentId}">client.agents.<a href="./src/browserbase/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/browserbase/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /v1/agents/{agentId}">client.agents.<a href="./src/browserbase/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/browserbase/types/agent_update_params.py">params</a>) -> <a href="./src/browserbase/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v1/agents">client.agents.<a href="./src/browserbase/resources/agents/agents.py">list</a>(\*\*<a href="src/browserbase/types/agent_list_params.py">params</a>) -> <a href="./src/browserbase/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agentId}">client.agents.<a href="./src/browserbase/resources/agents/agents.py">delete</a>(agent_id) -> None</code>

## Runs

Types:

```python
from browserbase.types.agents import (
    RunCreateResponse,
    RunRetrieveResponse,
    RunListResponse,
    RunListMessagesResponse,
)
```

Methods:

- <code title="post /v1/agents/runs">client.agents.runs.<a href="./src/browserbase/resources/agents/runs.py">create</a>(\*\*<a href="src/browserbase/types/agents/run_create_params.py">params</a>) -> <a href="./src/browserbase/types/agents/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /v1/agents/runs/{runId}">client.agents.runs.<a href="./src/browserbase/resources/agents/runs.py">retrieve</a>(run_id) -> <a href="./src/browserbase/types/agents/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/agents/runs">client.agents.runs.<a href="./src/browserbase/resources/agents/runs.py">list</a>(\*\*<a href="src/browserbase/types/agents/run_list_params.py">params</a>) -> <a href="./src/browserbase/types/agents/run_list_response.py">RunListResponse</a></code>
- <code title="get /v1/agents/runs/{runId}/messages">client.agents.runs.<a href="./src/browserbase/resources/agents/runs.py">list_messages</a>(run_id, \*\*<a href="src/browserbase/types/agents/run_list_messages_params.py">params</a>) -> <a href="./src/browserbase/types/agents/run_list_messages_response.py">RunListMessagesResponse</a></code>
