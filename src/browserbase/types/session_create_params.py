# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SessionCreateParams",
    "BrowserSettings",
    "BrowserSettingsContext",
    "BrowserSettingsFingerprint",
    "BrowserSettingsFingerprintScreen",
    "BrowserSettingsViewport",
    "ProxiesUnionMember0",
    "ProxiesUnionMember0UnionMember0",
    "ProxiesUnionMember0UnionMember0Geolocation",
    "ProxiesUnionMember0UnionMember1",
]


class SessionCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """The Project ID.

    Can be found in [Settings](https://www.browserbase.com/settings).
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

    proxies: Union[Iterable[ProxiesUnionMember0], bool]
    """Proxy configuration.

    Can be true for default proxy, or an array of proxy configurations.
    """

    region: Literal["us-west-2", "us-east-1", "eu-central-1", "ap-southeast-1"]
    """The region where the Session should run."""

    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """Duration in seconds after which the session will automatically end.

    Defaults to the Project's `defaultTimeout`.
    """

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


class BrowserSettingsFingerprintScreen(TypedDict, total=False):
    max_height: Annotated[int, PropertyInfo(alias="maxHeight")]

    max_width: Annotated[int, PropertyInfo(alias="maxWidth")]

    min_height: Annotated[int, PropertyInfo(alias="minHeight")]

    min_width: Annotated[int, PropertyInfo(alias="minWidth")]


class BrowserSettingsFingerprint(TypedDict, total=False):
    browsers: List[Literal["chrome", "edge", "firefox", "safari"]]

    devices: List[Literal["desktop", "mobile"]]

    http_version: Annotated[Literal["1", "2"], PropertyInfo(alias="httpVersion")]

    locales: SequenceNotStr[str]

    operating_systems: Annotated[
        List[Literal["android", "ios", "linux", "macos", "windows"]], PropertyInfo(alias="operatingSystems")
    ]

    screen: BrowserSettingsFingerprintScreen


class BrowserSettingsViewport(TypedDict, total=False):
    height: int
    """The height of the browser."""

    width: int
    """The width of the browser."""


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

    fingerprint: BrowserSettingsFingerprint
    """
    See usage examples
    [on the Stealth Mode page](/features/stealth-mode#fingerprinting)
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


class ProxiesUnionMember0UnionMember0Geolocation(TypedDict, total=False):
    country: Required[str]
    """Country code in ISO 3166-1 alpha-2 format"""

    city: str
    """Name of the city. Use spaces for multi-word city names. Optional."""

    state: str
    """US state code (2 characters). Must also specify US as the country. Optional."""


class ProxiesUnionMember0UnionMember0(TypedDict, total=False):
    type: Required[Literal["browserbase"]]
    """Type of proxy.

    Always use 'browserbase' for the Browserbase managed proxy network.
    """

    domain_pattern: Annotated[str, PropertyInfo(alias="domainPattern")]
    """Domain pattern for which this proxy should be used.

    If omitted, defaults to all domains. Optional.
    """

    geolocation: ProxiesUnionMember0UnionMember0Geolocation
    """Geographic location for the proxy. Optional."""


class ProxiesUnionMember0UnionMember1(TypedDict, total=False):
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


ProxiesUnionMember0: TypeAlias = Union[ProxiesUnionMember0UnionMember0, ProxiesUnionMember0UnionMember1]
