import time
import re
from playwright.sync_api import Page, expect

def test_verifyimage(page:Page):
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(2000)
    logo = page.get_by_alt_text("Image").first       #validate the image
    expect(logo).to_be_visible()
    page.close()


def test_verifyimagetext(page:Page):
    page.goto("https://u1.oliveboard.in/exams/?c=practice&i=banking")
    page.wait_for_timeout(10000)
    expect(page.get_by_text("Already a user?")).to_be_visible()        #validate the text
    expect(page.get_by_role("heading", name= "Sign Up")).to_be_visible()
    page.locator("#course-uphone").fill("9533447101")


def test_verifytitle(page: Page):
    page.goto("https://u1.oliveboard.in/exams/?c=practice&i=banking")
    expect(page.get_by_title("olive board"))
    expect(page.get_by_label("Email Id")).to_be_visible()
