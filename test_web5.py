from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

def test_history(browser):
    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    select.select_by_value("test.bat")

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'ctAgents')))

    agent = Select(driver.find_element_by_id("ctAgents"))
    agent.select_by_value("CerediraTess")
    request_button = driver.find_element_by_id("executeCTRequest")
    request_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table-bordered")))

    request_history = driver.find_elements(By.CSS_SELECTOR, "div.card")

    request_button.click()
    request_history_new = driver.find_elements(By.CSS_SELECTOR, "div.card")
    check = len(request_history_new) - len(request_history)

    assert check == 1, "Adding request history check"