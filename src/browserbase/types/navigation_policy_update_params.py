# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NavigationPolicyUpdateParams", "DomainOverride"]


class NavigationPolicyUpdateParams(TypedDict, total=False):
    allowed_categories: Annotated[
        List[
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
        ],
        PropertyInfo(alias="allowedCategories"),
    ]
    """Navigation categories.

    Browserbase blocks a domain in any blocked category, even if it is also in an
    allowed one.
    """

    blocked_categories: Annotated[
        List[
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
        ],
        PropertyInfo(alias="blockedCategories"),
    ]
    """Navigation categories.

    Browserbase blocks a domain in any blocked category, even if it is also in an
    allowed one.
    """

    default_decision: Annotated[Literal["allow", "block"], PropertyInfo(alias="defaultDecision")]
    """Decision for each of a domain's categories that has no category rule.

    The strictest of a domain's category decisions applies, and overrides take
    precedence.
    """

    description: str
    """Free-form notes about the policy."""

    domain_overrides: Annotated[Iterable[DomainOverride], PropertyInfo(alias="domainOverrides")]
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

    unknown_domain_behavior: Annotated[Literal["allow", "block"], PropertyInfo(alias="unknownDomainBehavior")]
    """Decision for a domain, or one of its categories, that Browserbase can't
    classify.

    It counts as one of the domain's category decisions, so the strictest still
    applies.
    """


class DomainOverride(TypedDict, total=False):
    decision: Required[Literal["allow", "block"]]
    """Decision for navigations to this host."""

    domain: Required[str]
    """Host the override applies to, for example `example.com`.

    Matching is case-insensitive and covers subdomains.
    """
