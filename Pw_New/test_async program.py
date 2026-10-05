
from playwright.async_api import async_playwright, Page, expect

import pytest

@pytest.mark.asyncio
async def test_pageURL():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        newtab = await browser.new_page()
        await newtab.goto("https://www.flipkart.com/")
        await expect(newtab).to_have_url("https://www.flipkart.com/")


