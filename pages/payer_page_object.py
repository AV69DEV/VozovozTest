from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class PayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

