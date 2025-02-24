import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/polls/")
    page.get_by_role("link", name="Do you like to travel ?").click()
    page.get_by_role("radio", name="Yes").check()
    page.get_by_role("button", name="Vote").click()
    page.get_by_role("link", name="Vote Again ?").click()
    page.get_by_role("button", name="Vote").click()
    page.get_by_role("button", name="Vote").click()
    page.get_by_role("button", name="Vote").click()
    page.locator("body").click()
    page.get_by_text("Do you like to travel ? You didn't select a choice. Yes No Perhaps Vote").click()
    page.locator("body").click()
    page.get_by_role("group", name="Do you like to travel ?").click()
    page.locator("body").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
