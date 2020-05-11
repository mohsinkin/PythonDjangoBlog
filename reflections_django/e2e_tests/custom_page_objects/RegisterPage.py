class RegisterPage:
    # textboxes
    username_name = "username"
    email_name = "email"
    password_name = "password1"
    confirm_password_name = "password2"

    # buttons
    sign_up_button_id = "sign_up"

    # messages
    register_message_xpath = "/html/body/main/div/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_box = self.driver.find_element_by_name(self.username_name)
        username_box.send_keys(username)

    def set_email(self, email):
        email_box = self.driver.find_element_by_name(self.email_name)
        email_box.send_keys(email)

    def set_password(self, password):
        password_box = self.driver.find_element_by_name(self.password_name)
        password_box.send_keys(password)

    def set_password_confirmation(self, password):
        password_confirm_box = self.driver.find_element_by_name(
            self.confirm_password_name
        )
        password_confirm_box.send_keys(password)

    def click_signup(self):
        self.driver.find_element_by_id(self.sign_up_button_id).click()

    def get_register_message(self):
        return self.driver.find_element_by_xpath(self.register_message_xpath).text
