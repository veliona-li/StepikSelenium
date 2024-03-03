from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_cart_btn()
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()
        self.check_name_product_added_to_cart()
        self.check_price_product_added_to_cart()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_name_product_added_to_cart(self):
        add_to_cart_message_name = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE_NAME).text
        assert add_to_cart_message_name == self.get_product_name(), \
            "Wrong product added to basket"

    def check_price_product_added_to_cart(self):
        add_to_cart_message_price = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE_PRICE).text
        assert self.get_product_price() == add_to_cart_message_price, \
            "Wrong product price added to basket"
