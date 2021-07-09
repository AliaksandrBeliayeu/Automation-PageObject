from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductsPageLocators
import time


class ProductsPage(BasePage):
    def adding_product_to_cart(self):
        book = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_BOOK)
        book_text = book.text
        price = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_PRICE)
        price_text = price.text
        adding_button = self.browser.find_element(*ProductsPageLocators.ADD_TO_BASKET)
        adding_button.click()
        #self.solve_quiz_and_get_code() # Can be enabled to pass tests with PROMO in URLS of the links used
        alert_book = self.browser.find_element(*ProductsPageLocators.ALERT_PRODUCT_ADDED)
        alert_book_text = alert_book.text
        alert_price = self.browser.find_element(*ProductsPageLocators.ALERT_CURRENT_PRICE)
        alert_price_text = alert_price.text
        assert book_text == alert_book_text, "ERROR: Incorrect Product Name is displayed in the Alert Message"
        assert price_text == alert_price_text, "ERROR: Incorrect Price is displayed in the Alert Message"

    def no_success_message_after_adding_product_to_basket(self):
        book = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_BOOK)
        book_text = book.text
        price = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_PRICE)
        price_text = price.text
        adding_button = self.browser.find_element(*ProductsPageLocators.ADD_TO_BASKET)
        adding_button.click()
        assert self.is_not_element_present(*ProductsPageLocators.ALERT_PRODUCT_ADDED), \
            "Success message is present, but should not be"

    def no_success_message_after_landing_on_page(self):
        book = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_BOOK)
        book_text = book.text
        price = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_PRICE)
        price_text = price.text
        adding_button = self.browser.find_element(*ProductsPageLocators.ADD_TO_BASKET)
        assert self.is_not_element_present(*ProductsPageLocators.ALERT_PRODUCT_ADDED), \
            "Success message is present, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        book = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_BOOK)
        book_text = book.text
        price = self.browser.find_element(*ProductsPageLocators.MAIN_PRODUCT_PRICE)
        price_text = price.text
        adding_button = self.browser.find_element(*ProductsPageLocators.ADD_TO_BASKET)
        adding_button.click()
        assert self.is_disappeared(*ProductsPageLocators.ALERT_PRODUCT_ADDED), \
            "Success message is present, but should not be"


