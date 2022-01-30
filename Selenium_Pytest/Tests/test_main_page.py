from pages.main_page import MainPage
from pages.locators import MainPageLocators


def test_guest_should_see_main_form(browser):
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.should_be_main_page()
        #time.sleep(5)



