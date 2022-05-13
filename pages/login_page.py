from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        mail_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        mail_input.send_keys(email)
        pass_input1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_input1.send_keys(password)
        pass_input2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        pass_input2.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button_reg.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
