import time

import pytest
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

def test_guest_should_see_login_form(browser):
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

class TestAddUserWithValidData():
    def test_add_user(self, browser):
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        email = "bvv_03@mail.ru"
        name = "bvv_03"
        password = "1234"
        page.should_not_be_authorised_user()
        page.register_new_user(name, email, password)
        page.should_be_authorised_user()
        page.exit_user()
        page.go_to_login_page()      
        page.delete_user(name)
    
    def test_add_user_with_existing_name(self, browser):
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        # регистрируем пользователя
        email = "bvv_03@mail.ru"
        name = "bvv_03"
        password = "1234"
        login_page = LoginPage(browser, browser.current_url)
        page.register_new_user(name, email, password)
        page.exit_user()
        page.go_to_login_page()      
        # регистрируем пользователя - имя уже есть в базе
        email = "bvv_00@mail.ru"
        name = "bvv_03"
        password = "1234"
        page.register_new_user(name, email, password)
        login_page.should_be_message_busy_name() # проверить на разных языках
        page.delete_user(name)

    def test_add_user_with_existing_email(self, browser):
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        # регистрируем пользователя
        email = "bvv_03@mail.ru"
        name = "bvv_03"
        password = "1234"
        login_page = LoginPage(browser, browser.current_url)
        page.register_new_user(name, email, password)
        page.exit_user()
        page.go_to_login_page()      
        # регистрируем пользователя - e-mail уже есть в базе
        email = "bvv_03@mail.ru"
        name = "bvv_00"
        password = "1234"
        page.register_new_user(name, email, password)
        login_page.should_be_message_busy_email()  # проверить на разных языках
        page.delete_user(email)

@pytest.mark.new
class TestAddUserWithWrongData():
        def test_add_user_with_wrong_email(self, browser, email, language):
            page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
            page.open()
            page.go_to_login_page()
            #email = "bvv_03mail.ru"
            name = "bvv_03"
            password = "1234"
            login_page = LoginPage(browser, browser.current_url)
            page.register_new_user(name, email, password)
            login_page.should_be_message_not_correct_email()  # проверить на разных языках
            login_page.should_be_correct_message_for_not_correct_email(language)
