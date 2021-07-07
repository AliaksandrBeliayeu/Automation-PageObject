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

class ProductsPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRODUCT_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main>:nth-child(1)")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>:nth-child(1)>:nth-child(2)>strong")
    ALERT_CURRENT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
