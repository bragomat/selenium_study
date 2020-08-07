from selenium.webdriver.support.ui import Select
from pages.CeredireaTess_page import CTPage


def test_auth(driver):
    ct_main = CTPage(driver)
    ct_main.login("usr_1", "1qaz@WSX")

    select = Select(driver.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Выберите скрипт для выполнения", "Authorisation check"
