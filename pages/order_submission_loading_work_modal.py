from pages.base_page import BasePage


class LoadingWorkModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.floor_input = None
        self.loading_works_switch = self.find_element_by_xpath('//*[contains(@content-desc,"Разгрузочные работы")]')
        self.service_lift = self.find_element_by_xpath('//android.widget.CheckBox[@content-desc="Грузовой лифт"]')
        self.confirm_button = self.find_element_by_xpath('//android.view.View[@content-desc="Подтвердить"]')

    def set_floor_input(self):
        self.floor_input = self.find_element_by_xpath('//android.widget.EditText')

    def click_loading_works_switch(self):
        self.loading_works_switch.click()

    def send_floor(self, floor: int):
        self.floor_input.click()
        self.floor_input.send_keys(f'{floor}')

    def click_service_lift(self):
        self.service_lift.click()

    def click_confirm_button(self):
        self.confirm_button.click()
