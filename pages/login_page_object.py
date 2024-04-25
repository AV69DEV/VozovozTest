from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_input = self.find_element_by_xpath("//*[@text='Телефон или Email*']")
        self.submit_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]')

    def send_login(self, keys):
        self.login_input.click()
        self.login_input.send_keys(keys)

    def click_submit(self):
        self.submit_button.click()
