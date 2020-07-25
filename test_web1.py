from selenium.webdriver.support.ui import Select


def test_auth(driver):
    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    check = select.first_selected_option.text

    assert check == "Выберите скрипт для выполнения", "Authorisation check"
