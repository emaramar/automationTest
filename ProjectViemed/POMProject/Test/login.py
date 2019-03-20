from selenium import webdriver
import unittest
import time
from ProjectViemed.POMProject.Pages.loginPage import LoginPage
from ProjectViemed.POMProject.Pages.homePage import Homepage


class LoginTest(unittest.TestCase):
    # execute the webdriver browser
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/emaramar/PycharmProjects/Edjel/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://telemed.viemed.io")
        login_text = driver.find_element_by_xpath("//p[@class='h4 text-center']").text
        self.assertEqual("Login",login_text,"The Login page is not displayed.")
        print("Login Page is displayed.")
        login.input_username("viemed.automation.tester@gmail.com")
        login.input_password("50BF57F3-523c-4082-9870-04eb33deab9e")
        login.click_login_button()
        return_txt = self.driver.find_element_by_xpath("//h2[contains(text(),'PROVIDER HOME')]").text
        self.assertEqual("PROVIDER HOME",return_txt, "The Home page is not displayed.")
        print("Login is successful.")
        time.sleep(10)

    def test_user_status(self):
        driver = self.driver
        home = Homepage(driver)
        home.btn_click()
        home.display_status()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        time.sleep(10)
        home = Homepage(driver)
        home.btn_click_logout()


if __name__ == '__main__':
    unittest.main()