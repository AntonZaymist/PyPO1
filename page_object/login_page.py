from constants import LOGIN_INCORRECT, PASS_INCORRECT
from page_object.base_page import BasePage
from page_object.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def get_login_form(self):
        return self.find_element(LoginPageLocators.LOGIN_FORM_LOCATORS)

    def get_register_form(self):
        return self.find_element(LoginPageLocators.REGISTER_FORM_LOCATORS)

    def get_title(self):
        return self.chrome_driver.title

    def try_to_login(self):
        email = self.find_element(LoginPageLocators.EMAIL_LOCATOR)
        email.send_keys(LOGIN_INCORRECT)
        password = self.find_element(LoginPageLocators.PASSWORD_LOCATOR)
        password.send_keys(PASS_INCORRECT)
        button = self.find_element(LoginPageLocators.BUTTON_LOGIN_LOCATOR)
        button.click()

    def get_oops(self):
        return self.find_element(LoginPageLocators.OOPS_LOCATOR)



