from Objects.Footer import Footer_Locators, Footer_Elements
from Objects.General_Locator import General_Locators
from Objects.Menu import Menu_Locators, Menu_Elements
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_cart_page(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_cart)
        General_Loc.element_locator_css(Menu_Elements.link_cart).click()

    def test_footer(self):
        Footer_Loc = Footer_Locators(self.driver)
        General_Loc = General_Locators(self.driver)

        Footer_Loc.goto_element_scroll(Footer_Elements.footer_element)

        try:
            assert General_Loc.element_locator_css(Footer_Elements.footer_sub_text).text
        except:
            print("Subscription Test is not displayed")

    def test_footer_email(self):
        Footer_Loc = Footer_Locators(self.driver)
        General_Loc = General_Locators(self.driver)

        Footer_Loc.subscribe("aki@gmail.com")

        try:
            assert General_Loc.element_locator_css(Footer_Elements.alert_success_subscribed).is_displayed()
        except:
            print("Correct alert is not displayed", General_Loc.element_locator_css(Footer_Elements.alert_success_subscribed).text)