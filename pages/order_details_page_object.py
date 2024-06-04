from pages.base_page import BasePage


class OrderDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.application_title = self.find_element_by_xpath('//android.view.View[@content-desc="• Заявка"]')
