# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import navigation_policy_create_params, navigation_policy_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.navigation_policy import NavigationPolicy
from ..types.navigation_policy_list_response import NavigationPolicyListResponse

__all__ = ["NavigationPoliciesResource", "AsyncNavigationPoliciesResource"]


class NavigationPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NavigationPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return NavigationPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NavigationPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return NavigationPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
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
        ]
        | Omit = omit,
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
        ]
        | Omit = omit,
        default_decision: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_overrides: Iterable[navigation_policy_create_params.DomainOverride] | Omit = omit,
        enabled: bool | Omit = omit,
        unknown_domain_behavior: Literal["allow", "block"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """Create a navigation policy for this project.

        Omitted fields take the defaults:
        enabled, block by default, block unknown domains, no category rules, and no
        overrides. Bind the policy to a session with `browserSettings.riskPolicyId`.

        Args:
          name: Display name. A policy's id identifies it, not its name.

          allowed_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          blocked_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          default_decision: Decision for each of a domain's categories that has no category rule. The
              strictest of a domain's category decisions applies, and overrides take
              precedence.

          description: Free-form notes about the policy.

          domain_overrides: Per-host decisions that take precedence over category rules and the default.
              Each host may appear once.

          enabled: Whether the policy can be bound to new sessions. Running sessions keep the
              policy they started with. A disabled policy stays editable and can be
              re-enabled.

          unknown_domain_behavior: Decision for a domain, or one of its categories, that Browserbase can't
              classify. It counts as one of the domain's category decisions, so the strictest
              still applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/navigation-policies",
            body=maybe_transform(
                {
                    "name": name,
                    "allowed_categories": allowed_categories,
                    "blocked_categories": blocked_categories,
                    "default_decision": default_decision,
                    "description": description,
                    "domain_overrides": domain_overrides,
                    "enabled": enabled,
                    "unknown_domain_behavior": unknown_domain_behavior,
                },
                navigation_policy_create_params.NavigationPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """
        Retrieve a single navigation policy by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/navigation-policies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    def update(
        self,
        id: str,
        *,
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
        ]
        | Omit = omit,
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
        ]
        | Omit = omit,
        default_decision: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_overrides: Iterable[navigation_policy_update_params.DomainOverride] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        unknown_domain_behavior: Literal["allow", "block"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """Update a navigation policy.

        Omitted fields keep their values; a supplied list
        replaces the stored list rather than adding to it. The change applies to
        sessions that start afterwards; running sessions keep the policy they started
        with.

        Args:
          allowed_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          blocked_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          default_decision: Decision for each of a domain's categories that has no category rule. The
              strictest of a domain's category decisions applies, and overrides take
              precedence.

          description: Free-form notes about the policy.

          domain_overrides: Per-host decisions that take precedence over category rules and the default.
              Each host may appear once.

          enabled: Whether the policy can be bound to new sessions. Running sessions keep the
              policy they started with. A disabled policy stays editable and can be
              re-enabled.

          name: Display name. A policy's id identifies it, not its name.

          unknown_domain_behavior: Decision for a domain, or one of its categories, that Browserbase can't
              classify. It counts as one of the domain's category decisions, so the strictest
              still applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/navigation-policies/{id}", id=id),
            body=maybe_transform(
                {
                    "allowed_categories": allowed_categories,
                    "blocked_categories": blocked_categories,
                    "default_decision": default_decision,
                    "description": description,
                    "domain_overrides": domain_overrides,
                    "enabled": enabled,
                    "name": name,
                    "unknown_domain_behavior": unknown_domain_behavior,
                },
                navigation_policy_update_params.NavigationPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicyListResponse:
        """List the project's navigation policies, ordered by name."""
        return self._get(
            "/v1/navigation-policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicyListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a navigation policy.

        New sessions can no longer bind to it; running
        sessions keep the policy they started with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/navigation-policies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNavigationPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNavigationPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNavigationPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNavigationPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncNavigationPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
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
        ]
        | Omit = omit,
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
        ]
        | Omit = omit,
        default_decision: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_overrides: Iterable[navigation_policy_create_params.DomainOverride] | Omit = omit,
        enabled: bool | Omit = omit,
        unknown_domain_behavior: Literal["allow", "block"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """Create a navigation policy for this project.

        Omitted fields take the defaults:
        enabled, block by default, block unknown domains, no category rules, and no
        overrides. Bind the policy to a session with `browserSettings.riskPolicyId`.

        Args:
          name: Display name. A policy's id identifies it, not its name.

          allowed_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          blocked_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          default_decision: Decision for each of a domain's categories that has no category rule. The
              strictest of a domain's category decisions applies, and overrides take
              precedence.

          description: Free-form notes about the policy.

          domain_overrides: Per-host decisions that take precedence over category rules and the default.
              Each host may appear once.

          enabled: Whether the policy can be bound to new sessions. Running sessions keep the
              policy they started with. A disabled policy stays editable and can be
              re-enabled.

          unknown_domain_behavior: Decision for a domain, or one of its categories, that Browserbase can't
              classify. It counts as one of the domain's category decisions, so the strictest
              still applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/navigation-policies",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allowed_categories": allowed_categories,
                    "blocked_categories": blocked_categories,
                    "default_decision": default_decision,
                    "description": description,
                    "domain_overrides": domain_overrides,
                    "enabled": enabled,
                    "unknown_domain_behavior": unknown_domain_behavior,
                },
                navigation_policy_create_params.NavigationPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """
        Retrieve a single navigation policy by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/navigation-policies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    async def update(
        self,
        id: str,
        *,
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
        ]
        | Omit = omit,
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
        ]
        | Omit = omit,
        default_decision: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_overrides: Iterable[navigation_policy_update_params.DomainOverride] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        unknown_domain_behavior: Literal["allow", "block"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicy:
        """Update a navigation policy.

        Omitted fields keep their values; a supplied list
        replaces the stored list rather than adding to it. The change applies to
        sessions that start afterwards; running sessions keep the policy they started
        with.

        Args:
          allowed_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          blocked_categories: Navigation categories. Browserbase blocks a domain in any blocked category, even
              if it is also in an allowed one.

          default_decision: Decision for each of a domain's categories that has no category rule. The
              strictest of a domain's category decisions applies, and overrides take
              precedence.

          description: Free-form notes about the policy.

          domain_overrides: Per-host decisions that take precedence over category rules and the default.
              Each host may appear once.

          enabled: Whether the policy can be bound to new sessions. Running sessions keep the
              policy they started with. A disabled policy stays editable and can be
              re-enabled.

          name: Display name. A policy's id identifies it, not its name.

          unknown_domain_behavior: Decision for a domain, or one of its categories, that Browserbase can't
              classify. It counts as one of the domain's category decisions, so the strictest
              still applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/navigation-policies/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "allowed_categories": allowed_categories,
                    "blocked_categories": blocked_categories,
                    "default_decision": default_decision,
                    "description": description,
                    "domain_overrides": domain_overrides,
                    "enabled": enabled,
                    "name": name,
                    "unknown_domain_behavior": unknown_domain_behavior,
                },
                navigation_policy_update_params.NavigationPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicy,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavigationPolicyListResponse:
        """List the project's navigation policies, ordered by name."""
        return await self._get(
            "/v1/navigation-policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationPolicyListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a navigation policy.

        New sessions can no longer bind to it; running
        sessions keep the policy they started with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/navigation-policies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NavigationPoliciesResourceWithRawResponse:
    def __init__(self, navigation_policies: NavigationPoliciesResource) -> None:
        self._navigation_policies = navigation_policies

        self.create = to_raw_response_wrapper(
            navigation_policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            navigation_policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            navigation_policies.update,
        )
        self.list = to_raw_response_wrapper(
            navigation_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            navigation_policies.delete,
        )


class AsyncNavigationPoliciesResourceWithRawResponse:
    def __init__(self, navigation_policies: AsyncNavigationPoliciesResource) -> None:
        self._navigation_policies = navigation_policies

        self.create = async_to_raw_response_wrapper(
            navigation_policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            navigation_policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            navigation_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            navigation_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            navigation_policies.delete,
        )


class NavigationPoliciesResourceWithStreamingResponse:
    def __init__(self, navigation_policies: NavigationPoliciesResource) -> None:
        self._navigation_policies = navigation_policies

        self.create = to_streamed_response_wrapper(
            navigation_policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            navigation_policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            navigation_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            navigation_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            navigation_policies.delete,
        )


class AsyncNavigationPoliciesResourceWithStreamingResponse:
    def __init__(self, navigation_policies: AsyncNavigationPoliciesResource) -> None:
        self._navigation_policies = navigation_policies

        self.create = async_to_streamed_response_wrapper(
            navigation_policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            navigation_policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            navigation_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            navigation_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            navigation_policies.delete,
        )
