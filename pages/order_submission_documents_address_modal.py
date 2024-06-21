from pages.base_page import BasePage


class OrderSubmissionDocumentsAtTheAddressModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address_input = self.find_element_by_xpath('//android.widget.EditText[@hint="Поиск по названию улицы"]')

    def send_address(self, test_documents_address):
        self.address_input.click()
        self.address_input.send_keys(test_documents_address)

    def get_valid_street_entity(self, street: str):

        street_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.view.View")]')

        for ent in street_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc").__contains__(f"{street}"):
                return ent
