from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_an_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Empty basket message is presented"

    def should_not_be_message_an_empty_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Empty basket message is presented, but should not be"
