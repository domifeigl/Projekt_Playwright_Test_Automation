from playwright.sync_api import Page, sync_playwright
import pytest


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.czechitas.cz/")
        page.locator('text="Zamítnout vše"').click()
        yield page
        browser.close()


def test_find_course(page: Page):
    page.locator("#w-dropdown-toggle-0 > div").hover()
    page.locator('text="Kalendář"').first.click()
    page.locator("#Search-Input").fill("python")
    kurz = page.locator('text="Úvod do Pythonu"').nth(1)
    assert kurz.is_visible()


def test_sign_up(page: Page):
    page.locator("#w-dropdown-toggle-0 > div").hover()
    page.locator('text="Katalog kurzů"').click()
    with page.expect_popup() as new_popup:
        page.locator('text="SQL"').click()
    popup = new_popup.value
    popup.locator("a.button.more.w-button").click()
    signup = popup.locator("#snippet--flashes > div > div > div.toast-body")
    signup.wait_for()
    prihlaseni = popup.locator("#kt_app_body")
    assert prihlaseni.is_visible()


def test_log_in(page: Page):
    with page.expect_popup() as new_pop_up:
        page.locator(".moje-czechitas-icon").click()
    pop_up = new_pop_up.value
    pop_up.locator("#frm-slotLoader-singIn-signIn-form-login").fill("email@email.cz")
    pop_up.locator("#frm-slotLoader-singIn-signIn-form-password").fill("abcdef")
    pop_up.get_by_role("checkbox").check()
    button = pop_up.locator(".btn.btn-primary.button")
    button.press("Enter")
    success = pop_up.locator('text="Vítej v Czechitas"').nth(1)
    assert success.is_visible()== False
