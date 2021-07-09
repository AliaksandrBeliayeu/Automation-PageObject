from .locators import BasePageLocators
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def empty_basket_alert(self):
        empty_basket_alert = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_LABEL)
        text = empty_basket_alert.text
        assert text == "Your basket is empty. Continue shopping"