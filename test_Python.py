from playwright.sync_api import Page


def test_find_course(page: Page):
    page.goto("https://www.czechitas.cz/")
    page.locator("#ch2-dialog > div.ch2-dialog-actions.ch2-dialog-actions-vertical > button.ch2-btn.ch2-allow-all-btn.ch2-btn-primary").click()
    page.locator("#w-dropdown-toggle-0 > div").hover()
    page.locator("#w-dropdown-list-0 > a:nth-child(1)").click()
    page.locator("#Search-Input").fill("python")
    kurz = page.locator("#top > div.container.kalendar.custom_calendar.w-container > div.collection-list-wrapper-11.w-dyn-list > div.all-events-list.w-dyn-items > div:nth-child(2) > div.event-info-block > a")
    assert kurz.is_visible()


def test_sign_up(page: Page):
    page.goto("https://www.czechitas.cz/")
    page.locator("#ch2-dialog > div.ch2-dialog-actions.ch2-dialog-actions-vertical > button.ch2-btn.ch2-allow-all-btn.ch2-btn-primary").click()
    page.locator("#w-dropdown-toggle-0 > div").hover()
    page.locator("#w-dropdown-list-0 > a:nth-child(4)").click()
    with page.expect_popup() as new_popup:
        page.locator("body > div.katalog_main > div.container-10.w-container > div.w-dyn-list > div > div:nth-child(8) > a > div").click()
    popup = new_popup.value
    popup.locator("#Terminy > div > div.section-title-wrapper > div.w-dyn-list > div > div > div.lide-a-registrace.pl-0 > div.ikony-term-nu.cena > a.button.more.w-button").click()
    prihlaseni = popup.locator("#kt_app_body")
    assert prihlaseni.is_visible()


def test_log_in(page: Page):
    page.goto("https://www.czechitas.cz/")
    page.locator("#ch2-dialog > div.ch2-dialog-actions.ch2-dialog-actions-vertical > button.ch2-btn.ch2-allow-all-btn.ch2-btn-primary").click()
    with page.expect_popup() as new_pop_up:
        page.locator("body > div.header-wrapper > div.navbar.w-nav > div.navcontainer.w-container > nav > div.mobileflex > a").click()
    pop_up = new_pop_up.value
    pop_up.locator("#frm-slotLoader-singIn-signIn-form-login").fill("email@email.cz")
    pop_up.locator("#frm-slotLoader-singIn-signIn-form-password").fill("abcdef")
    pop_up.get_by_role("checkbox").check()
    button = pop_up.locator("#frm-slotLoader-singIn-signIn-form > div:nth-child(3) > input")
    button.press("Enter")
    error = pop_up.locator("#snippet--flashes > div > div > div.toast-body")
    assert error.is_visible()
