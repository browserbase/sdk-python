# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RunCreateParams", "BrowserSettings", "BrowserSettingsContext", "Variables"]


class RunCreateParams(TypedDict, total=False):
    task: Required[str]
    """A natural language description of the task the agent should accomplish."""

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """
    Optionally run a specific [custom agent](/reference/api/create-an-agent) you've
    created by ID. The run will use the agent's `systemPrompt` and `resultSchema`
    unless overridden.
    """

    browser_settings: Annotated[BrowserSettings, PropertyInfo(alias="browserSettings")]
    """Browser configuration for the agent's session.

    When omitted, runner defaults apply.
    """

    result_schema: Annotated[Dict[str, object], PropertyInfo(alias="resultSchema")]
    """An optional [JSON Schema](https://json-schema.org/specification) object.

    If provided, the agent will aim to return a `result` that conforms to this
    schema when the run completes. Overrides the referenced agent's default
    `resultSchema` for this run only.
    """

    variables: Dict[str, Variables]
    """Optional named variables the agent can reference as placeholders, i.e.

    `%variable%`. Each entry pairs a `value` the placeholder resolves to with an
    optional `description` that hints to the agent when it should be used. Values
    are not persisted.
    """


class BrowserSettingsContext(TypedDict, total=False):
    id: Required[str]
    """The Context ID."""

    persist: bool
    """Whether to persist the context after browsing. Defaults to false."""


class BrowserSettings(TypedDict, total=False):
    """Browser configuration for the agent's session.

    When omitted, runner defaults apply.
    """

    context: BrowserSettingsContext

    proxies: bool
    """Set true to route the agent's browser session through the default proxy."""

    verified: bool
    """Set true to enable Browserbase Verified for the session."""


class Variables(TypedDict, total=False):
    value: Required[str]
    """The value the placeholder resolves to when the agent uses it."""

    description: str
    """
    Optional hint to the agent describing what this variable represents and when to
    use it.
    """
