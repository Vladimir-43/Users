from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/user/login/index.html" in self.browser.current_url, "Wrong Login or register link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_E_MAIL), "Login e-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), \
            "Submit Button in Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_NAME), "Register name is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_E_MAIL), "Register e-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT_BUTTON), \
            "Submit Button in Register form is not presented"

    def should_be_message_busy_name(self):
        assert self.is_presented_text_in_element(*LoginPageLocators.REGISTER_MESSAGE), \
            "Busy name message is not presented"

    def should_be_message_busy_email(self):
        assert self.is_presented_text_in_element(*LoginPageLocators.REGISTER_MESSAGE), \
            "Busy email message is not presented"

    def should_be_message_not_correct_email(self):
        assert self.is_presented_text_in_element(*LoginPageLocators.REGISTER_MESSAGE), \
            "'register_not_correct_field(email)' message is not presented"

    def should_be_correct_message_for_not_correct_email(self, lng):
        if lng == "en":
            assert self.is_equally_text_in_element(*LoginPageLocators.REGISTER_MESSAGE, \
                                                   "register_not_correct_field (email)"), \
                                                   "Correct message is not presented"
        elif lng == "ru":
            assert self.is_equally_text_in_element(*LoginPageLocators.REGISTER_MESSAGE, \
                                                   "Неправильное значение поля (email)"), \
                                                   "Correct message is not presented"
