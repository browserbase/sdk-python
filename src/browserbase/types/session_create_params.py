# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SessionCreateParams",
    "BrowserSettings",
    "BrowserSettingsContext",
    "BrowserSettingsViewport",
    "ProxiesUnionArrayVariant1",
    "ProxiesUnionArrayVariant1BrowserbaseProxyConfig",
    "ProxiesUnionArrayVariant1BrowserbaseProxyConfigGeolocation",
    "ProxiesUnionArrayVariant1ExternalProxyConfig",
    "ProxiesUnionArrayVariant1NoneProxyConfig",
]


class SessionCreateParams(TypedDict, total=False):
    api_timeout: int
    """Duration in seconds after which the session will automatically end.

    Defaults to the Project's `defaultTimeout`.
    """

    browser_settings: Annotated[BrowserSettings, PropertyInfo(alias="browserSettings")]

    extension_id: Annotated[str, PropertyInfo(alias="extensionId")]
    """The uploaded Extension ID.

    See [Upload Extension](/reference/api/upload-an-extension).
    """

    keep_alive: Annotated[bool, PropertyInfo(alias="keepAlive")]
    """Set to true to keep the session alive even after disconnections.

    Available on the Hobby Plan and above.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The Project ID.

    Can be found in [Settings](https://www.browserbase.com/settings).
    """

    proxies: Union[bool, Iterable[ProxiesUnionArrayVariant1]]
    """Proxy configuration.

    Can be true for default proxy, or an array of proxy configurations.
    """

    region: Literal["us-west-2", "us-east-1", "eu-central-1", "ap-southeast-1"]
    """The region where the Session should run."""

    user_metadata: Annotated[Dict[str, object], PropertyInfo(alias="userMetadata")]
    """Arbitrary user metadata to attach to the session.

    To learn more about user metadata, see
    [User Metadata](/features/sessions#user-metadata).
    """


class BrowserSettingsContext(TypedDict, total=False):
    id: Required[str]
    """The Context ID."""

    persist: bool
    """Whether or not to persist the context after browsing. Defaults to `false`."""


class BrowserSettingsViewport(TypedDict, total=False):
    height: int

    width: int


class BrowserSettings(TypedDict, total=False):
    advanced_stealth: Annotated[bool, PropertyInfo(alias="advancedStealth")]
    """Advanced Browser Stealth Mode"""

    block_ads: Annotated[bool, PropertyInfo(alias="blockAds")]
    """Enable or disable ad blocking in the browser. Defaults to `false`."""

    captcha_image_selector: Annotated[str, PropertyInfo(alias="captchaImageSelector")]
    """Custom selector for captcha image.

    See [Custom Captcha Solving](/features/stealth-mode#custom-captcha-solving)
    """

    captcha_input_selector: Annotated[str, PropertyInfo(alias="captchaInputSelector")]
    """Custom selector for captcha input.

    See [Custom Captcha Solving](/features/stealth-mode#custom-captcha-solving)
    """

    context: BrowserSettingsContext

    extension_id: Annotated[str, PropertyInfo(alias="extensionId")]
    """The uploaded Extension ID.

    See [Upload Extension](/reference/api/upload-an-extension).
    """

    log_session: Annotated[bool, PropertyInfo(alias="logSession")]
    """Enable or disable session logging. Defaults to `true`."""

    os: Literal["windows", "mac", "linux", "mobile", "tablet"]
    """Operating system for stealth mode.

    Valid values: windows, mac, linux, mobile, tablet
    """

    record_session: Annotated[bool, PropertyInfo(alias="recordSession")]
    """Enable or disable session recording. Defaults to `true`."""

    solve_captchas: Annotated[bool, PropertyInfo(alias="solveCaptchas")]
    """Enable or disable captcha solving in the browser. Defaults to `true`."""

    viewport: BrowserSettingsViewport


class ProxiesUnionArrayVariant1BrowserbaseProxyConfigGeolocation(TypedDict, total=False):
    """Configuration for geolocation"""

    country: Required[str]
    """Country code in ISO 3166-1 alpha-2 format"""

    city: str
    """Name of the city. Use spaces for multi-word city names. Optional."""

    state: str
    """US state code (2 characters). Must also specify US as the country. Optional."""


class ProxiesUnionArrayVariant1BrowserbaseProxyConfig(TypedDict, total=False):
    type: Required[Literal["browserbase"]]
    """Type of proxy.

    Always use 'browserbase' for the Browserbase managed proxy network.
    """

    domain_pattern: Annotated[str, PropertyInfo(alias="domainPattern")]
    """Domain pattern for which this proxy should be used.

    If omitted, defaults to all domains. Optional.
    """

    geolocation: ProxiesUnionArrayVariant1BrowserbaseProxyConfigGeolocation
    """Configuration for geolocation"""


class ProxiesUnionArrayVariant1ExternalProxyConfig(TypedDict, total=False):
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


class ProxiesUnionArrayVariant1NoneProxyConfig(TypedDict, total=False):
    domain_pattern: Required[Annotated[str, PropertyInfo(alias="domainPattern")]]
    """Domain pattern for which site should have proxies disabled."""

    type: Required[Literal["none"]]
    """Type of proxy. Use 'none' to disable proxy for matching domains."""


ProxiesUnionArrayVariant1: TypeAlias = Union[
    ProxiesUnionArrayVariant1BrowserbaseProxyConfig,
    ProxiesUnionArrayVariant1ExternalProxyConfig,
    ProxiesUnionArrayVariant1NoneProxyConfig,
]
