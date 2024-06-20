from pages.base_page import BasePage


class OrderSubmissionDocumentsAtTheAddressModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address_input = self.find_element_by_xpath('//android.widget.EditText[@class="Поиск по названию улицы"]')
