from playwright.sync_api import sync_playwright
import time
from cookie_handler import read_and_modify_cookies
from comment_screenshotter.captureparentdiv import PlaywrightScraper  # assuming your class is in this module

def run(playwright):
    browser = playwright.firefox.launch(headless=False,
                                        firefox_user_prefs={"media.peerconnection.enabled": False})
    context = browser.new_context()
    page = context.new_page()

    cookies = read_and_modify_cookies('C:/Users/elija/Desktop/TikTokCookie.txt')
    context.add_cookies(cookies)

    page.goto('https://www.tiktok.com/@jadennewmannn/video/7307074993781837087')
    time.sleep(10)

    scraper = PlaywrightScraper(page)
    found = scraper.search_text_and_screenshot('ion run it')

    if found:
        print("Text found and screenshot taken.")
    else:
        print("Text not found within the given time.")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
