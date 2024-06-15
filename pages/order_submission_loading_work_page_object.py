from pages.base_page import BasePage


class LoadingWorkPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.floor_input = self.find_element_by_xpath('//android.widget.EditText')
        self.service_lift = self.find_element_by_xpath('//android.widget.CheckBox[@content-desc="Грузовой лифт"]')
        self.confirm_button = self.find_element_by_xpath('//android.view.View[@content-desc="Подтвердить"]')

    def send_floor(self, floor: int):
        self.floor_input.click()
        self.floor_input.send_keys(f'{floor}')

    def click_service_lift(self):
        self.service_lift.click()

    def click_confirm_button(self):
        self.confirm_button.click()



