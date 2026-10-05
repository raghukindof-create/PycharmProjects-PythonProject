
from playwright.sync_api import Page,expect

def test_displayURL(page:Page):
    page.goto("https://www.flipkart.com/")
    myurl = page.url
    print("the application url is", myurl)
    expect(page).to_have_url( "https://www.flipkart.com/", )


def test_displayTitle(page:Page):
    page.goto("https://www.flipkart.com/")
    title=page.title()
    print("title is",title)
    expect(page).to_have_title( "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!" )