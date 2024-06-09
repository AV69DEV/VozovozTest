from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class RecipientIndividualsPageIndividuals(BasePage):
    name_input = None

    def __init__(self, driver):
        super().__init__(driver)
        self.name_input = self.find_element_by_xpath('//*[contains(@hint,"ФИО*")]')
        self.basic_phone_input = self.find_element_by_xpath('//*[contains(@hint, "Основной *")]')
        self.name_search_button = self.find_element_by_uiautomator(
            'new UiSelector().className("android.view.View").instance(12)')
        self.mail_title = self.find_element_by_xpath('//android.view.View[@content-desc="Почта"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_name_input(self):
        self.name_input.click()

    def click_search_button(self):
        self.name_search_button.click()

    def click_save_button(self):
        self.save_button.click()


class RecipientIndividualsSearchSubpageObject(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_input = self.find_element_by_xpath('//*[contains(@hint, "Имя/телефон или др.")]')

    def send_name(self, name):
        self.name_input.send_keys(name)

    def check_for_valid_counterparty(self, name, phone) -> bool:
        valid_element_is_presented = False
        counterparty_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.widget.ImageView")]')

        for ent in counterparty_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc") == f"{name} \n{phone}":
                valid_element_is_presented = True

        return valid_element_is_presented

    def get_valid_counterparty(self, name, phone):

        counterparty_entities = self.find_elements(
            '//*[contains(@package, "ru.vozovoz.customers") and contains(@class, "android.widget.ImageView")]')

        for ent in counterparty_entities:
            print(ent.get_attribute("content-desc"))
            if ent.get_attribute("content-desc") == f"{name} \n{phone}":
                return ent
