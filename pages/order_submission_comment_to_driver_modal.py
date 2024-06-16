from pages.base_page import BasePage


class OrderSubmissionCommentToDriverModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.comment_input = self.find_element_by_xpath('//*[contains(@class, "android.widget.EditText")]')
        self.confirm_button = self.find_element_by_xpath('//android.view.View[@content-desc="Подтвердить"]')

    def send_comment(self, text: str):
        self.click_comment_input()
        self.comment_input.send_keys(text)

    def click_comment_input(self):
        self.comment_input.click()

    def click_confirm_button(self):
        self.confirm_button.click()

