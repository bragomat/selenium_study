import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:

    def __init__(self, driver):
        self.driver = driver

        self.search_input = driver.find_element_by_xpath("//input[@title='Поиск']")
        self.search_submit = driver.find_element_by_xpath("//input[@value='Поиск в Google']")

    def search_something(self, key_for_search):
        self.search_input.send_keys(key_for_search)
        #WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.search_submit))
        time.sleep(1)
        self.search_submit.click()
