from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

def pytest_configure(config):
    print("\n*******StartUp*******")


@pytest.fixture()
def browser():
    global driver
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.get("http://127.0.0.1:4444/CerediraTess.html")
    driver.maximize_window()
    yield
    time.sleep(2)
    driver.quit()


def test_no_agent(browser):
    # username = driver.find_element_by_id("username")
    # username.send_keys("usr_1")
    # password = driver.find_element_by_id("password")
    # password.send_keys("1qaz@WSX")
    # submit = driver.find_element_by_id("updateCT")
    # submit.click()

    check = "\nНе выбраны"
    print(check)
    # _text = driver.find_element_by_id("errorModalBody")
    # _text_2 = _text.text
    # assert check in _text_2
