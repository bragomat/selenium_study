from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    driver = webdriver.Chrome("driver\chromedriver.exe")
    driver.get("http://127.0.0.1:4444/CerediraTess.html")

    username = driver.find_element_by_id("username")
    username.send_keys("fake_user")
    password = driver.find_element_by_id("password")
    password.send_keys("fake_pass")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Авторизуйтесь, для получения доступных скриптов", "Authorisation fail check"

finally:
    time.sleep(10)
    driver.quit()