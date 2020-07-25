from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_ctagent(driver):
    username = driver.find_element_by_id("username")
    username.send_keys("usr_1")
    password = driver.find_element_by_id("password")
    password.send_keys("1qaz@WSX")
    submit = driver.find_element_by_id("updateCT")
    submit.click()

    select = Select(driver.find_element_by_id("ctScripts"))
    select.select_by_value("test.bat")

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'ctAgents')))

    agents = driver.find_elements(By.XPATH, '//*[@id="ctAgents"]/option[not(@disabled)]')

    assert len(agents) > 0, "Check available agents"

    ct_agent = driver.find_elements(By.XPATH, '//*[@id="ctAgents"]/option[@value="CerediraTess"]')

    assert ct_agent, "Check CerediraTess-agent is available"
