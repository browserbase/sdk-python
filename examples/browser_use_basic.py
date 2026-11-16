#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["browserbase>=1.26.0", "browser-use>=1.0.6,<2", "python-dotenv"]
# ///
# browser-use needs Python 3.11+, so this runs in its own environment: `uv run examples/browser_use_basic.py`.
# Lint runs on 3.9 without browser-use installed:
# mypy: ignore-errors
# pyright: basic, reportMissingImports=false
import os
import asyncio

from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatAnthropic

from browserbase import Browserbase

load_dotenv(override=True)

bb = Browserbase(api_key=os.environ["BROWSERBASE_API_KEY"])


async def run(llm: object) -> None:
    session = bb.sessions.create()
    print(f"Session: https://www.browserbase.com/sessions/{session.id}")

    # cdp_url, not browser-use 0.x's wss_url: connect_url speaks CDP, not Playwright's protocol.
    browser = Browser(cdp_url=session.connect_url)
    try:
        agent = Agent(
            task="Open https://news.ycombinator.com and return the title of the top story.",
            llm=llm,
            browser=browser,
        )
        history = await agent.run()
        print(history.final_result())
    finally:
        # stop() only disconnects from a cdp_url browser; release the session so it stops billing.
        await browser.stop()
        bb.sessions.update(session.id, status="REQUEST_RELEASE")
    print("Done!")


if __name__ == "__main__":
    asyncio.run(run(ChatAnthropic(model="claude-sonnet-5-5")))
