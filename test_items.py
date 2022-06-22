import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_should_be_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    check_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    check_button_text = check_button.text
    assert check_button, "Кнопки нет на странице"
