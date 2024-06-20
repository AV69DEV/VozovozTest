from pages.base_page import BasePage


class OrderSubmissionDriverData(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = self.find_element_by_xpath('//android.widget.EditText[@hint="Email *"]')
        self.confirm_button = self.find_element_by_xpath('//android.view.View[@content-desc="Подтвердить"]')

    def send_email(self, email):
        self.email_input.click()
        self.email_input.send_keys(email)

    def click_confirm_button(self):
        self.confirm_button.click()
