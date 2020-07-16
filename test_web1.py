from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest
import time

@pytest.fixture()
def browser():
    browser = webdriver.Chrome("driver/chromedriver.exe")
    browser.get("http://127.0.0.1:4444/CerediraTess.html")
    browser.maximize_window()
    yield browser
    time.sleep(2)
    browser.quit()

def test_auth(browser):
    username = browser.find_element_by_id("username")
    username.send_keys("usr_1")
    password = browser.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = browser.find_element_by_id("updateCT")
    submit.click()

    select = Select(browser.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Выберите скрипт для выполнения", "Authorisation check"