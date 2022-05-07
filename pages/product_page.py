from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in \
               self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, \
               "Message about adding product not found"

    def should_be_message_total_price(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Message about total price not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message hasn't disappeared."
