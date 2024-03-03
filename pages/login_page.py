from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        email_input = self.element_is_present(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.element_is_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = self.element_is_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        register_btn = self.element_is_present(*LoginPageLocators.REGISTER_BUTTON)
        register_btn.click()
