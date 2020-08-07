import pytest
from selenium import webdriver

link = "http://127.0.0.1:4444/CerediraTess.html"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture()
def driver(request):
    driver_name = request.config.getoption("browser_name")
    driver = None
    if driver_name == "chrome":
        driver = webdriver.Chrome("driver/chromedriver.exe")
    elif driver_name == "firefox":
        driver = webdriver.Firefox(executable_path="driver/geckodriver.exe")
    elif driver_name == "edge":
        driver = webdriver.Edge("driver/msedgedriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or edge")
    driver.get(link)
    driver.maximize_window()
    yield driver
    driver.quit()
