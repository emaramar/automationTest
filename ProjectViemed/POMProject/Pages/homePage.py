from ProjectViemed.POMProject.Locators.locators import Locators

class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.provider_text = Locators.provider_text
        # self.display_status = Locators.

    def display_text_provider(self):
        homepage = self.driver.find_element_by_xpath(self.provider_text).text
        print("This is the:"+homepage)

    def display_status(self):
        status = self.driver.find_element_by_xpath("//div[contains(text(),'Your status is')]").text
        print(status)

    def btn_click(self):
        btn_busy = self.driver.find_element_by_xpath("//button[contains(text(),'Busy')]")
        btn_free = self.driver.find_element_by_xpath("//button[contains(text(),'Free')]")

        while not btn_busy.is_enabled() and not btn_free.is_enabled():
            print " "

        if btn_busy.is_enabled():
            btn_busy.click()
        else:
            btn_free.click()

    def btn_click_logout(self):
        self.driver.find_element_by_xpath("//a[@class='nav-link']").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'Log out')]").click()
        self.driver.close()