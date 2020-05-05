class LoginPage:
    # textboxes
    username_id = "username"
    password_id = "password"

    # buttons
    login_button = "login_button"
    logout_button = "logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_box = self.driver.find_element_by_name(self.username_id)
        username_box.send_keys(username)

    def set_password(self, password):
        password_box = self.driver.find_element_by_name(self.password_id)
        password_box.send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button).click()
