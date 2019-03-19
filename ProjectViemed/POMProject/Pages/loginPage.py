from ProjectViemed.POMProject.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id

    def input_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def input_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath("//div[@class='text-center']").click()

    def check_login_text(self):
        self.driver.find_element_by_xpath("//p[@class='h4 text-center']").text