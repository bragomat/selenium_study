

class CTPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_input = driver.find_element_by_id("username")
        self.password_input = driver.find_element_by_id("password")
        self.login_submit = driver.find_element_by_id("updateCT")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_submit.click()

