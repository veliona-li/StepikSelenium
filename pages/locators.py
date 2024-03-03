from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_QUANTITY = (By.CSS_SELECTOR, "#content_inner p.col-sm-3.h3")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button[type='submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
    ADD_TO_CART_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    ADD_TO_CART_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")

