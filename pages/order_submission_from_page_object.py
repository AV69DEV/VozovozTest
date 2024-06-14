from pages.base_page import BasePage


class OrderSubmissionFromPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_by_city_button = self.find_element_by_xpath('//*[contains(@content-desc,"Поиск по городу")]')
        self.address_button = self.find_element_by_xpath('//android.view.View[@content-desc="Адрес"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_search_by_city_button(self):
        self.search_by_city_button.click()

    def click_address_button(self):
        self.address_button.click()

    def click_save_button(self):
        self.save_button.click()

    def check_address(self, address: str):
        branch_element = self.find_element_by_xpath(f'//android.widget.RadioButton[@content-desc="{address}"]')


class SearchByCityModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.city_input = self.find_element_by_uiautomator('new UiSelector().className("android.widget.EditText")')

    def send_city(self, city):
        self.city_input.send_keys(city)

    def get_valid_city_entity(self, city: str):

        city_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.widget.ImageView")]')

        for ent in city_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc").__contains__(f"{city}\n"):
                return ent


class AddressSubPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_by_street_button = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Поиск по названию улицы"]')
        self.map_button = self.find_element_by_uiautomator('new UiSelector().className("android.widget.ImageView")')

    def click_search_by_street_button(self):
        self.search_by_street_button.click()

    def click_map_button(self):
        self.map_button.click()

    def check_displayed_street(self, street_to_search):
        self.find_element_by_xpath(f'//android.view.View[@content-desc="{street_to_search}"]')


class MapSubPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.find_element_by_xpath('//android.widget.RelativeLayout/android.view.View')


class SearchByStreetModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.street_input = self.find_element_by_xpath('//android.widget.EditText')

    def send_street(self, street: str):
        self.street_input.send_keys(street)

    def get_valid_street_entity(self, street: str):

        street_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.view.View")]')

        for ent in street_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc").__contains__(f"{street}"):
                return ent

    def clik_select_address_manually(self):
        self.find_element_by_xpath('//*[contains(@content-desc, "Внимание!")]').click()
