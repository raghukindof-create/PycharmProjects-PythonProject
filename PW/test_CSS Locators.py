from playwright.sync_api import Page, expect

def test_css_locators(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#name").fill("Raghu")
    page.locator(".form-control[maxlength='25']").fill("raghava2356@gmail.com")
    page.locator(".form-control[maxlength='10']").fill("9533447101")
    page.wait_for_timeout(5000)

