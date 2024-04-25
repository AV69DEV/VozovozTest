from pages.base_page import BasePage


class PasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_input = self.find_element_by_xpath("//*[@text='Пароль']")
        self.submit_button = self.find_element_by_xpath('//android.view.View[@content-desc="Войти"]')

    def send_password(self, keys):
        self.password_input.click()
        self.password_input.send_keys(keys)

    def click_submit(self):
        self.submit_button.click()
