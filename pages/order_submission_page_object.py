from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class OrderSubmissionPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]', time=20)
        self.from_ = self.find_element_by_xpath('//*[contains(@content-desc,"Откуда")]', time=20)
        self.date_ = self.find_element_by_xpath('//*[contains(@content-desc,"Дата")]', time=20)
        self.time_ = self.find_element_by_xpath('//*[contains(@content-desc,"Время")]', time=20)

        """self.some_element = self.driver.find_element(by=appiumby.AppiumBy.XPATH,
                                                      value="//*[contains(text(),'Откуда')]")"""

    def click_next_button(self):
        self.next_button.click()

    def next_button_is_presented(self):
        self.next_button.is_displayed()
