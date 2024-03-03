import pytest
import time

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

# LINK_BOOK_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LINK_BOOK = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
LINK_LOGIN = "https://selenium1py.pythonanywhere.com/accounts/login/"
LINK_BOOK_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
LINK_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LINK_LOGIN)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK_BOOK)
        page.open()
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK_BOOK)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK_BOOK_PROMO)
    page.open()
    page.add_product_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('promo', [*range(7),
                                   pytest.param("7", marks=pytest.mark.xfail),
                                   *range(8, 10)])
def test_guest_can_add_product_to_basket_parametrize(browser, promo):
    link = f"{LINK_PROMO}{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_BOOK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_BOOK)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK_BOOK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK_BOOK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK_BOOK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.basket_is_empty()
