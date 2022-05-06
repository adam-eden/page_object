from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_add_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Message about adding product not found"

    def should_be_message_total_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE) ==  \
               self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Message about total price not found"




