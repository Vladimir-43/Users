from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import LoginPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    # Проверка, что элемент на странице 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Проверка, что элемент не появляется на странице в течение заданного времени. 
    # Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def register_new_user(self, name, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_NAME).send_keys(name)
        self.browser.find_element(*LoginPageLocators.REGISTER_E_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()

    def exit_user(self):
        self.browser.find_element(*MainPageLocators.USER_ICON).click()
        self.browser.find_element(*MainPageLocators.EXIT_BUTTON).click()

    def delete_user(self, user_name):
        self.logining_manager()
        self.browser.find_element(*MainPageLocators.SEARCH_NAME_EMAIL).send_keys(user_name)
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()
        self.browser.find_element(*MainPageLocators.DELETE_BUTTON).click()
        # план - поймать всплывающее окно подтверждения, проверить имя пользователя (.notifications.bottom-right)

    def logining_manager(self):
        email = "manager@mail.ru"
        password = "1"
        self.logining_user(email, password)

    def logining_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_E_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def open(self):
        self.browser.get(self.url)
    
    def should_be_authorised_user(self):
        assert self.is_element_present(*MainPageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

    def should_not_be_authorised_user(self):
        assert self.is_not_element_present(*MainPageLocators.USER_ICON), "User icon is presented," \
                                                                 " probably authorised user"

    def is_presented_text_in_element(self, how, what):
        if self.browser.find_element(how, what).text:
            return True
        else:
            return False

    def is_equally_text_in_elements(self, first_how, first_what, second_how, second_what):
        if self.browser.find_element(first_how, first_what).text == \
                self.browser.find_element(second_how, second_what).text:
            return True
        else:
            return False

    def is_equally_text_in_element(self, how, what, text):
        if text in self.browser.find_element(how, what).text:
            return True
        else:
            return False
