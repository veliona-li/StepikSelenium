from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        basket_is_empty_message = self.element_is_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert "Your basket is empty" in basket_is_empty_message.text, \
            "Basket is empty message is wrong"

    def should_not_be_product_in_basket(self):
        basket_quantity = self.is_not_element_present(*BasketPageLocators.BASKET_QUANTITY)
        assert basket_quantity, "Basket is not empty, but should be"
