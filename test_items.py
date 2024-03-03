import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")


def test_presence_of_btn_to_basket(browser):
    """Check Add To Basket Button is present"""
    browser.get(URL)

    # команда добавлена для визуальной проверки фразы на кнопке добавления в корзину (критерий оценивания)
    time.sleep(30)

    add_to_basket_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located(ADD_TO_BASKET))
    # browser.execute_script("return arguments[0].scrollIntoView(true);", add_to_basket_button)

    # time.sleep(5)

    assert add_to_basket_button is not None, "Button is not visible"
