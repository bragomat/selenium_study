from time import sleep

from selenium import webdriver
import pytest

driver = None


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def test_google(test_setup):
    driver.get("https://www.google.com/")
    sleep(2)
