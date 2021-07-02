from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name = 'login-username']")
    LOGIN_PW = (By.CSS_SELECTOR, "[name = 'login-password']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name = 'login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REGISTRATION_PW1 = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REGISTRATION_PW2 = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit']")
