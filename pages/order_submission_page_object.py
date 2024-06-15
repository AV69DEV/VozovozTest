from appium.webdriver.webdriver import WebDriver
from pages.base_page import BasePage


class OrderSubmissionPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]', timeout=20)
        self.from_ = self.find_element_by_xpath('//*[contains(@content-desc,"Откуда")]', timeout=20)
        self.date_ = self.find_element_by_xpath('//*[contains(@content-desc,"Дата")]', timeout=20)
        self.time_ = self.find_element_by_xpath('//*[contains(@content-desc,"Время")]', timeout=20)
        self.loading_work_ = None
        self.comment_to_the_driver_ = None
        self.driving_directions_ = None
        self.driver_data_ = None
        self.documents_at_the_address_ = None
        self.special_requirements_and_transport_ = None

    def click_next_button(self):
        self.next_button.click()

    def next_button_is_presented(self):
        self.next_button.is_displayed()

    def click_from_(self):
        self.from_.click()

    def initialize_additional_fields(self):
        self.loading_work_ = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Погрузочные работы")]')
        self.comment_to_the_driver_ = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Комментарий водителю"]')
        self.driving_directions_ = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Схема проезда"]')
        self.driver_data_ = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Данные водителя"]')
        self.documents_at_the_address_ = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Документы по адресу"]')
        self.special_requirements_and_transport_ = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Спец. требования и транспорт"]')
