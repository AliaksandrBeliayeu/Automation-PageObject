import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.base_page import BasePage




def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    page.empty_basket_alert()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    page.empty_basket_alert()