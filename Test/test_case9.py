from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Objects.Menu import Menu_Locators
from Objects.Products import Products_locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.link_locator(Menu_Loc.link_products).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Link not displayed",triggeredException)

        Menu_Loc.link_locator(Menu_Loc.link_products).click()

    def test_product_page(self):
        Products_loc = Products_locators(self.driver)

        Products_loc.explicitly_wait_element_css(Products_loc.product_header_element)

        try:
            assert Products_loc.element_locator_css(Products_loc.product_header_element).is_displayed()
        except NoSuchElementException as triggeredException:
            print("All Products header is not displayed", triggeredException)

    def test_search_product(self):
        searchProductData = csvReader.csvReader(csvReader.searchProductData)
        Products_loc = Products_locators(self.driver)

        Products_loc.search_product(searchProductData[0]['Product_Name'])

    def test_searched_products(self):
        searchProductData = csvReader.csvReader(csvReader.searchProductData)
        search_product = searchProductData[0]['Product_Name']
        Products_loc = Products_locators(self.driver)

        Products_name = Products_loc.product_list(Products_loc.product_name_element)


        for product in Products_name:
            try:
                assert search_product.casefold() in product.text.casefold()
            except:
                print(product.text,"is not equal with searched product")



