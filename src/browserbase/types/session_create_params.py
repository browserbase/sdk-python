# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SessionCreateParams",
    "BrowserSettings",
    "BrowserSettingsContext",
    "BrowserSettingsFingerprint",
    "BrowserSettingsFingerprintScreen",
    "BrowserSettingsViewport",
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

    This is available on the Startup plan only.
    """

    proxies: object
    """Proxy configuration.

    Can be true for default proxy, or an array of proxy configurations.
    """

    region: Literal["us-west-2", "us-east-1", "eu-central-1", "ap-southeast-1"]
    """The region where the Session should run."""


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

    http_version: Annotated[Literal[1, 2], PropertyInfo(alias="httpVersion")]

    locales: List[str]
    """
    Full list of locales is available
    [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language).
    """

    operating_systems: Annotated[
        List[Literal["android", "ios", "linux", "macos", "windows"]], PropertyInfo(alias="operatingSystems")
    ]
    """
    Note: `operatingSystems` set to `ios` or `android` requires `devices` to include
    `"mobile"`.
    """

    screen: BrowserSettingsFingerprintScreen


class BrowserSettingsViewport(TypedDict, total=False):
    height: int

    width: int


class BrowserSettings(TypedDict, total=False):
    block_ads: Annotated[bool, PropertyInfo(alias="blockAds")]
    """Enable or disable ad blocking in the browser. Defaults to `false`."""

    context: BrowserSettingsContext

    extension_id: Annotated[str, PropertyInfo(alias="extensionId")]
    """The uploaded Extension ID.

    See [Upload Extension](/reference/api/upload-an-extension).
    """

    fingerprint: BrowserSettingsFingerprint
    """
    See usage examples
    [in the Stealth Mode page](/features/stealth-mode#fingerprinting).
    """

    log_session: Annotated[bool, PropertyInfo(alias="logSession")]
    """Enable or disable session logging. Defaults to `true`."""

    record_session: Annotated[bool, PropertyInfo(alias="recordSession")]
    """Enable or disable session recording. Defaults to `true`."""

    solve_captchas: Annotated[bool, PropertyInfo(alias="solveCaptchas")]
    """Enable or disable captcha solving in the browser. Defaults to `true`."""

    viewport: BrowserSettingsViewport
