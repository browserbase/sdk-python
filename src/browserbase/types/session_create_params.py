# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams", "BrowserSettings", "BrowserSettingsContext", "BrowserSettingsViewport"]


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

    proxies: Union[bool, object]
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
