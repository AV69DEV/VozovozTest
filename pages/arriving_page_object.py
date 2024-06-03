from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class ArrivingPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]')
        self.direction_ = self.find_element_by_xpath('//*[contains(@content-desc,"Куда")]')
        self.date_ = self.find_element_by_xpath('//*[contains(@content-desc,"Дата")]')
        self.time_ = self.find_element_by_xpath('//*[contains(@content-desc,"Время")]')

    def click_next_button(self):
        self.next_button.click()