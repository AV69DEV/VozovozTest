from appium.webdriver.webdriver import WebDriver
from pages.base_page import BasePage
from util.Exceptions import Exceptions

CityNotFoundExec = Exceptions()


class ArrivingWherePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.search_by_city_button = self.find_element_by_xpath('//*[contains(@content-desc,"Поиск по городу")]')
        self.address_button = self.find_element_by_xpath('//android.view.View[@content-desc="Адрес"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_search_by_city_button(self):
        self.search_by_city_button.click()

    def click_address_button(self):
        self.address_button.click()

    def click_save_button(self):
        self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')
        self.save_button.click()


class SearchByCityModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.city_input = self.find_element_by_uiautomator('new UiSelector().className("android.widget.EditText")')

    def send_city(self, city):
        self.city_input.send_keys(city)

    def get_valid_city_entity(self, city: str):

        city_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.widget.ImageView")]')
        print(city_entities)

        for ent in city_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc").__contains__(f"{city}\n"):
                return ent
        print(f'Ошибка - Искомый город {city} не найден в списке')
        assert 1 == 0  #Необходим был ассерт который будет всегда падать

    def check_if_nothing_found_banner_here(self):
        nothing_found_banner = self.find_element_by_xpath('//*[contains(@content-desc,"Ничего не найдено")]')


class AddressSubPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_by_street_button = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Поиск по названию улицы"]')
        self.map_button = self.find_element_by_uiautomator(
            'new UiSelector().className("android.widget.ImageView")')

    def click_search_by_street_button(self, address=''):
        self.search_by_street_button = self.find_element_by_xpath(
            f'//android.view.View[@content-desc="Поиск по названию улицы" or @content-desc="{address}"]')
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

    def get_valid_street_entity(self, street: str, building_number=''):

        street_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.view.View")]')

        for ent in street_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc").casefold().__contains__(f"{street}") and ent.get_attribute(
                    "content-desc").__contains__(f"{building_number}"):
                return ent

    def clik_select_address_manually(self):
        self.find_element_by_xpath('//*[contains(@content-desc, "Внимание!")]').click()
