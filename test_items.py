import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_should_be_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
