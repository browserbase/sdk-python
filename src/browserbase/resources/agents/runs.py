# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import run_list_params, run_create_params, run_list_messages_params
from ...types.agents.run_list_response import RunListResponse
from ...types.agents.run_create_response import RunCreateResponse
from ...types.agents.run_retrieve_response import RunRetrieveResponse
from ...types.agents.run_list_messages_response import RunListMessagesResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        task: str,
        agent_id: str | Omit = omit,
        browser_settings: run_create_params.BrowserSettings | Omit = omit,
        result_schema: Dict[str, object] | Omit = omit,
        variables: Dict[str, run_create_params.Variables] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Run a browser agent to complete the `task` by using web search and browser
        tooling. Optionally pass `agentId` to run a
        [custom agent](/reference/api/create-an-agent) you've created.

        Args:
          task: A natural language description of the task the agent should accomplish.

          agent_id: Optionally run a specific [custom agent](/reference/api/create-an-agent) you've
              created by ID. The run will use the agent's `systemPrompt` and `resultSchema`
              unless overridden.

          browser_settings: Browser configuration for the agent's session. When omitted, runner defaults
              apply.

          result_schema: An optional [JSON Schema](https://json-schema.org/specification) object. If
              provided, the agent will aim to return a `result` that conforms to this schema
              when the run completes. Overrides the referenced agent's default `resultSchema`
              for this run only.

          variables: Optional named variables the agent can reference as placeholders, i.e.
              `%variable%`. Each entry pairs a `value` the placeholder resolves to with an
              optional `description` that hints to the agent when it should be used. Values
              are not persisted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/runs",
            body=maybe_transform(
                {
                    "task": task,
                    "agent_id": agent_id,
                    "browser_settings": browser_settings,
                    "result_schema": result_schema,
                    "variables": variables,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Retrieve the current status and details of a run, including its result and
        associated session information. To fetch the run's messages, use
        [List Run Messages](/reference/api/list-run-messages).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/agents/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveResponse,
        )

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        cursor: str | Omit = omit,
        end_at: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "STOPPED", "TIMED_OUT"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """List runs across your account.

        Supports filtering by status, by the agent they
        reference, and by creation time.

        Args:
          agent_id: Only return runs that reference this agent ID.

          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

          end_at: Only return runs created on or before this timestamp (inclusive). ISO 8601 / RFC
              3339, e.g. 2026-01-20T00:00:00Z.

          limit: Maximum number of results to return.

          start_at: Only return runs created on or after this timestamp (inclusive). ISO 8601 / RFC
              3339, e.g. 2026-01-19T00:00:00Z.

          status: Current status of the run.

              - `PENDING` - agent will run soon
              - `RUNNING` - agent is currently running
              - `COMPLETED` - agent has finished running
              - `FAILED` - agent has failed the run
              - `STOPPED` - run was stopped by the user
              - `TIMED_OUT` - run exceeded maximum time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/agents/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "cursor": cursor,
                        "end_at": end_at,
                        "limit": limit,
                        "start_at": start_at,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def list_messages(
        self,
        run_id: str,
        *,
        all: bool | Omit = omit,
        limit: int | Omit = omit,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListMessagesResponse:
        """
        Returns a paginated list of messages produced by a run, in chronological order,
        with the oldest messages first.

        Messages conform to the
        [AI SDK UIMessage format](https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message).

        Args:
          all: Return every message after `since` in one response, ignoring `limit`.

          limit: Maximum number of messages to return.

          since: The `id` of the last message you've already received. The response will contain
              messages produced after that one, in chronological order. Omit on the first
              call. Pass the previous response's `nextSince` value to continue paging or to
              poll for new messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/agents/runs/{run_id}/messages", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all": all,
                        "limit": limit,
                        "since": since,
                    },
                    run_list_messages_params.RunListMessagesParams,
                ),
            ),
            cast_to=RunListMessagesResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browserbase/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browserbase/sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        task: str,
        agent_id: str | Omit = omit,
        browser_settings: run_create_params.BrowserSettings | Omit = omit,
        result_schema: Dict[str, object] | Omit = omit,
        variables: Dict[str, run_create_params.Variables] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Run a browser agent to complete the `task` by using web search and browser
        tooling. Optionally pass `agentId` to run a
        [custom agent](/reference/api/create-an-agent) you've created.

        Args:
          task: A natural language description of the task the agent should accomplish.

          agent_id: Optionally run a specific [custom agent](/reference/api/create-an-agent) you've
              created by ID. The run will use the agent's `systemPrompt` and `resultSchema`
              unless overridden.

          browser_settings: Browser configuration for the agent's session. When omitted, runner defaults
              apply.

          result_schema: An optional [JSON Schema](https://json-schema.org/specification) object. If
              provided, the agent will aim to return a `result` that conforms to this schema
              when the run completes. Overrides the referenced agent's default `resultSchema`
              for this run only.

          variables: Optional named variables the agent can reference as placeholders, i.e.
              `%variable%`. Each entry pairs a `value` the placeholder resolves to with an
              optional `description` that hints to the agent when it should be used. Values
              are not persisted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/runs",
            body=await async_maybe_transform(
                {
                    "task": task,
                    "agent_id": agent_id,
                    "browser_settings": browser_settings,
                    "result_schema": result_schema,
                    "variables": variables,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Retrieve the current status and details of a run, including its result and
        associated session information. To fetch the run's messages, use
        [List Run Messages](/reference/api/list-run-messages).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/agents/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveResponse,
        )

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        cursor: str | Omit = omit,
        end_at: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "STOPPED", "TIMED_OUT"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """List runs across your account.

        Supports filtering by status, by the agent they
        reference, and by creation time.

        Args:
          agent_id: Only return runs that reference this agent ID.

          cursor: Pagination cursor. Pass the nextCursor from the previous response to fetch the
              next page. Omit to start from the first page.

          end_at: Only return runs created on or before this timestamp (inclusive). ISO 8601 / RFC
              3339, e.g. 2026-01-20T00:00:00Z.

          limit: Maximum number of results to return.

          start_at: Only return runs created on or after this timestamp (inclusive). ISO 8601 / RFC
              3339, e.g. 2026-01-19T00:00:00Z.

          status: Current status of the run.

              - `PENDING` - agent will run soon
              - `RUNNING` - agent is currently running
              - `COMPLETED` - agent has finished running
              - `FAILED` - agent has failed the run
              - `STOPPED` - run was stopped by the user
              - `TIMED_OUT` - run exceeded maximum time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/agents/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "cursor": cursor,
                        "end_at": end_at,
                        "limit": limit,
                        "start_at": start_at,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def list_messages(
        self,
        run_id: str,
        *,
        all: bool | Omit = omit,
        limit: int | Omit = omit,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListMessagesResponse:
        """
        Returns a paginated list of messages produced by a run, in chronological order,
        with the oldest messages first.

        Messages conform to the
        [AI SDK UIMessage format](https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message).

        Args:
          all: Return every message after `since` in one response, ignoring `limit`.

          limit: Maximum number of messages to return.

          since: The `id` of the last message you've already received. The response will contain
              messages produced after that one, in chronological order. Omit on the first
              call. Pass the previous response's `nextSince` value to continue paging or to
              poll for new messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/agents/runs/{run_id}/messages", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all": all,
                        "limit": limit,
                        "since": since,
                    },
                    run_list_messages_params.RunListMessagesParams,
                ),
            ),
            cast_to=RunListMessagesResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.list_messages = to_raw_response_wrapper(
            runs.list_messages,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.list_messages = async_to_raw_response_wrapper(
            runs.list_messages,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.list_messages = to_streamed_response_wrapper(
            runs.list_messages,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            runs.list_messages,
        )
