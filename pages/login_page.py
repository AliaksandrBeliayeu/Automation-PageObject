from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login substring is missing in the URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login Email Field is NOT present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PW), "Login Password Field is NOT present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login Submit button is NOT present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration Email Field is NOT present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PW1), "Registration New Password Field is NOT present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PW2), "Registration New Password Confirmation Field is NOT present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration Submit button is NOT present"

    def register_new_user(self):
        new_user_email = str(time.time()) + "@fakemail.org"
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email_field.send_keys(new_user_email)
        new_user_password ='ACDCDIO1a'
        new_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PW1)
        new_password_field.send_keys(new_user_password)
        confirmation_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PW2)
        confirmation_password_field.send_keys(new_user_password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        submit.click()


