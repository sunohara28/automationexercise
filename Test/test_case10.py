from Objects.Footer import Footer_Locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_footer(self):
        Footer_Loc = Footer_Locators(self.driver)

        Footer_Loc.goto_element_scroll(Footer_Loc.footer_element)
        try:
            assert Footer_Loc.element_locator_css(Footer_Loc.footer_sub_text).text
        except:
            print("Subscription Test is not displayed")

    def test_footer_email(self):
        Footer_Loc = Footer_Locators(self.driver)

        Footer_Loc.element_send_keys(Footer_Loc.element_locator_id(Footer_Loc.footer_email_textbox),"aki@gmail.com")
        Footer_Loc.element_click(Footer_Loc.element_locator_id(Footer_Loc.footer_button))

        try:
            assert Footer_Loc.element_locator_css(Footer_Loc.alert_success_subscribed).is_displayed()
        except:
            print("Correct alert is not displayed", Footer_Loc.element_locator_css(Footer_Loc.alert_success_subscribed).text)

