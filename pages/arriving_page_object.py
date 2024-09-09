from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class ArrivingPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]', timeout=20)
        self.where_ = self.find_element_by_xpath('//*[contains(@content-desc,"Куда")]', timeout=20)
        self.date_ = self.find_element_by_xpath('//*[contains(@content-desc,"Дата")]', timeout=20)
        self.time_ = self.find_element_by_xpath('//*[contains(@content-desc,"Время")]', timeout=20)
        self.unloading_work_ = None
        self.comment_to_driver_ = None
        self.driving_directions_ = None
        self.driver_data_ = None
        self.documents_at_the_address_ = None
        self.special_requirements_and_transport_ = None

    def click_date_(self):
        self.date_.click()

    def click_next_button(self):
        self.next_button.click()

    def next_button_is_presented(self):
        self.next_button.is_displayed()

    def click_where_button(self):
        self.where_.click()

    def click_comment_to_driver_(self):
        self.comment_to_driver_.click()

    def click_diving_directions_(self):
        self.driving_directions_.click()

    def click_driver_data_(self):
        self.driver_data_.click()

    def click_documents_at_the_address(self):
        self.documents_at_the_address_.click()

    def click_special_requirements_and_transport_(self):
        self.special_requirements_and_transport_.click()

    def initialize_additional_fields(self):
        self.unloading_work_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Разгрузочные работы")]')
        self.comment_to_driver_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Комментарий водителю")]')
        self.driving_directions_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Схема проезда")]')
        self.driver_data_ = self.find_element_by_xpath('//*[contains(@content-desc,"Данные водителя")]')
        self.documents_at_the_address_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Документы по адресу")]')
        self.special_requirements_and_transport_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Спец. требования и транспорт")]')
