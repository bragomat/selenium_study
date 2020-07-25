import pytest
from selenium import webdriver

link = "http://127.0.0.1:4444/CerediraTess.html"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.get(link)
    driver.maximize_window()
    yield driver
    driver.quit()
