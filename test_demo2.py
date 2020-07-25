from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Demo import GooglePage
import pytest
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("driver/chromedriver.exe")
    browser.maximize_window()
    yield browser
    time.sleep(2)
    browser.quit()


def test_auth(browser):
    browser.get("https://www.google.com/")
    time.sleep(3)
    google = GooglePage(browser)
    google.search_something("666")
