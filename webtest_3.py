from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    driver = webdriver.Chrome("driver\chromedriver.exe")
    driver.get("http://127.0.0.1:4444/CerediraTess.html")

    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    select.select_by_index(1)
    time.sleep(2)

    agent = Select(driver.find_element_by_id("ctAgents"))
    agent.select_by_value("CerediraTess")
    request_button = driver.find_element_by_id("executeCTRequest")
    request_button.click()
    time.sleep(2)

    checkbox = driver.find_element_by_css_selector("div.card-body td:last-child")
    check = checkbox.text

    assert check == "SUCCESS", "Request completion check"

finally:
    time.sleep(5)
    driver.quit()