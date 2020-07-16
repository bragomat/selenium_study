from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_authfail(browser):
    username = driver.find_element_by_id("username")
    username.send_keys("fake_user")
    password = driver.find_element_by_id("password")
    password.send_keys("fake_pass")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    select = Select(driver.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Авторизуйтесь, для получения доступных скриптов", "Authorisation fail check"