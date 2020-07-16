from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest
import time

@pytest.fixture()
def browser():
    global driver
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.get("http://127.0.0.1:4444/CerediraTess.html")
    driver.maximize_window()
    yield
    time.sleep(2)
    driver.quit()

def test_auth(browser):
    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Выберите скрипт для выполнения", "Authorisation check"