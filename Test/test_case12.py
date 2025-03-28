import time

from selenium.common import NoSuchElementException
from Objects.Menu import Menu_Locators
from Objects.Products import Products_locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_product_page(self):
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.link_locator(Menu_Loc.link_products).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Link not displayed",triggeredException)

        Menu_Loc.link_locator(Menu_Loc.link_products).click()

    def test_add_to_cart(self):
        Products_loc = Products_locators(self.driver)

        Products_loc.product_hover(2)
        Products_loc.product_add_to_cart(2)

        Products_loc.modal_button_click(Products_loc.modal_view_cart_element)
        time.sleep(2)





