# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NavigationPolicy", "DomainOverride"]


class DomainOverride(BaseModel):
    decision: Literal["allow", "block"]
    """Decision for navigations to this host."""

    domain: str
    """Host the override applies to, for example `example.com`.

    Matching is case-insensitive and covers subdomains.
    """


class NavigationPolicy(BaseModel):
    """Rules for which domains a browser session may navigate to.

    Bind a policy to a session with `browserSettings.riskPolicyId`; Browserbase then allows or blocks each navigation by the policy's overrides, its category rules, and finally its default decision. A session keeps the policy as it was when the session started: edits, disables, and deletes apply to sessions that start afterwards. A policy checks navigations: page loads, iframes, popups, and each redirect. It doesn't check requests a page makes itself, such as scripts, images, and `fetch` calls. In a session that loads a Context, pages skip their service workers so that the policy checks every navigation.
    """

    id: str
    """Unique identifier for the navigation policy."""

    allowed_categories: List[
        Literal[
            "adult",
            "ai-tools",
            "alcohol-tobacco",
            "business",
            "child-abuse",
            "communication",
            "dating",
            "drugs",
            "education",
            "entertainment",
            "finance",
            "gambling",
            "games",
            "government-military",
            "hacking",
            "hate",
            "health",
            "illegal-activity",
            "infrastructure",
            "kids",
            "lifestyle",
            "malware",
            "newly-registered",
            "news",
            "parked-inactive",
            "phishing-scams",
            "piracy",
            "proxy-anonymizer",
            "search-portal",
            "self-harm",
            "shopping",
            "social-media",
            "society-culture",
            "sports",
            "technology",
            "terrorism-extremism",
            "travel",
            "url-shortener",
            "violence",
            "weapons",
        ]
    ] = FieldInfo(alias="allowedCategories")
    """Navigation categories.

    Browserbase blocks a domain in any blocked category, even if it is also in an
    allowed one.
    """

    blocked_categories: List[
        Literal[
            "adult",
            "ai-tools",
            "alcohol-tobacco",
            "business",
            "child-abuse",
            "communication",
            "dating",
            "drugs",
            "education",
            "entertainment",
            "finance",
            "gambling",
            "games",
            "government-military",
            "hacking",
            "hate",
            "health",
            "illegal-activity",
            "infrastructure",
            "kids",
            "lifestyle",
            "malware",
            "newly-registered",
            "news",
            "parked-inactive",
            "phishing-scams",
            "piracy",
            "proxy-anonymizer",
            "search-portal",
            "self-harm",
            "shopping",
            "social-media",
            "society-culture",
            "sports",
            "technology",
            "terrorism-extremism",
            "travel",
            "url-shortener",
            "violence",
            "weapons",
        ]
    ] = FieldInfo(alias="blockedCategories")
    """Navigation categories.

    Browserbase blocks a domain in any blocked category, even if it is also in an
    allowed one.
    """

    created_at: datetime = FieldInfo(alias="createdAt")

    default_decision: Literal["allow", "block"] = FieldInfo(alias="defaultDecision")
    """Decision for each of a domain's categories that has no category rule.

    The strictest of a domain's category decisions applies, and overrides take
    precedence.
    """

    description: str
    """Free-form notes about the policy."""

    domain_overrides: List[DomainOverride] = FieldInfo(alias="domainOverrides")
    """Per-host decisions that take precedence over category rules and the default.

    Each host may appear once.
    """

    enabled: bool
    """Whether the policy can be bound to new sessions.

    Running sessions keep the policy they started with. A disabled policy stays
    editable and can be re-enabled.
    """

    name: str
    """Display name. A policy's id identifies it, not its name."""

    project_id: str = FieldInfo(alias="projectId")
    """The project the policy belongs to."""

    unknown_domain_behavior: Literal["allow", "block"] = FieldInfo(alias="unknownDomainBehavior")
    """Decision for a domain, or one of its categories, that Browserbase can't
    classify.

    It counts as one of the domain's category decisions, so the strictest still
    applies.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
