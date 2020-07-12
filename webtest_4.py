from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    driver = webdriver.Chrome("driver\chromedriver.exe")
    driver.get("http://127.0.0.1:4444/CerediraTess.html")
    driver.maximize_window()

    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    select.select_by_value("test.bat")

    request_button = driver.find_element_by_id("executeCTRequest")
    request_button.click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer button")))

finally:
    time.sleep(2)
    driver.quit()