# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RunCreateParams",
    "BrowserSettings",
    "BrowserSettingsContext",
    "BrowserSettingsProxiesUnionMember0",
    "BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfig",
    "BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfigGeolocation",
    "BrowserSettingsProxiesUnionMember0ExternalProxyConfig",
    "BrowserSettingsProxiesUnionMember0NoneProxyConfig",
    "Variables",
]


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


class BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfigGeolocation(TypedDict, total=False):
    """Geographic location for the proxy. Optional."""

    country: Required[str]
    """Country code in ISO 3166-1 alpha-2 format"""

    city: str
    """Name of the city. Use spaces for multi-word city names. Optional."""

    state: str
    """US state code (2 characters). Must also specify US as the country. Optional."""


class BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfig(TypedDict, total=False):
    type: Required[Literal["browserbase"]]
    """Type of proxy.

    Always use 'browserbase' for the Browserbase managed proxy network.
    """

    domain_pattern: Annotated[str, PropertyInfo(alias="domainPattern")]
    """Domain pattern for which this proxy should be used.

    If omitted, defaults to all domains. Optional.
    """

    geolocation: BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfigGeolocation
    """Geographic location for the proxy. Optional."""


class BrowserSettingsProxiesUnionMember0ExternalProxyConfig(TypedDict, total=False):
    server: Required[str]
    """Server URL for external proxy. Required."""

    type: Required[Literal["external"]]
    """Type of proxy. Always 'external' for this config."""

    domain_pattern: Annotated[str, PropertyInfo(alias="domainPattern")]
    """Domain pattern for which this proxy should be used.

    If omitted, defaults to all domains. Optional.
    """

    password: str
    """Password for external proxy authentication. Optional."""

    username: str
    """Username for external proxy authentication. Optional."""


class BrowserSettingsProxiesUnionMember0NoneProxyConfig(TypedDict, total=False):
    type: Required[Literal["none"]]
    """Type of proxy. Always 'none' for this config."""

    domain_pattern: Annotated[str, PropertyInfo(alias="domainPattern")]
    """Domain pattern for which this proxy should be used.

    If omitted, defaults to all domains. Optional.
    """


BrowserSettingsProxiesUnionMember0: TypeAlias = Union[
    BrowserSettingsProxiesUnionMember0BrowserbaseProxyConfig,
    BrowserSettingsProxiesUnionMember0ExternalProxyConfig,
    BrowserSettingsProxiesUnionMember0NoneProxyConfig,
]


class BrowserSettings(TypedDict, total=False):
    """Browser configuration for the agent's session.

    When omitted, runner defaults apply.
    """

    context: BrowserSettingsContext

    proxies: Union[Iterable[BrowserSettingsProxiesUnionMember0], bool]
    """Proxy configuration.

    Can be true for default proxy, or an array of proxy configurations.
    """

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
