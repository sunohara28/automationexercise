from selenium.common import NoSuchElementException

from Objects.Menu import Menu_Locators
from Objects.Products import Products_locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        assert Menu_Loc.link_locator(Menu_Loc.link_products).is_displayed()
        Menu_Loc.link_locator(Menu_Loc.link_products).click()

    def test_products(self):
        Products_loc = Products_locators(self.driver)

        Products_loc.explicity_wait_element_xpath(Products_loc.header_all_products)

        try:
            assert Products_loc.element_locator_xpath(Products_loc.header_all_products).is_displayed()
        except NoSuchElementException as triggeredException:
            print("All Products header is not displayed",triggeredException)