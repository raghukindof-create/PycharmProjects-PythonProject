from playwright.async_api import Page, expect, async_playwright
import pytest

@pytest.mark.asyncio

async def test_pageurl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.flipkart.com/")
        await expect(page).to_have_url( "https://www.flipkart.com/")