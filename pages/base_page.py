import locale
import time
from datetime import date

import appium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common import appiumby
from selenium.common.exceptions import StaleElementReferenceException


def get_weekday_string(value: int):
    if value == 0:
        return 'пн'
    elif value == 1:
        return 'вт'
    elif value == 2:
        return 'ср'
    elif value == 3:
        return 'чт'
    elif value == 4:
        return 'пт'
    elif value == 5:
        return 'сб'
    elif value == 6:
        return 'вс'


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.ignored_exceptions = (StaleElementReferenceException,)

    def find_element_by_xpath(self, locator: str, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)),
                                                         message=f"Can't find element by locator: {locator}")

    def find_element_by_xpath_with_ignored_exceptions(self, locator: str, ignored_exceptions, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, locator)),
            message=f"Can't find element by locator: {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((By.XPATH, locator)),
                                                         message=f"Can't find elements by locator: {locator}")

    def find_element_by_uiautomator(self, locator: str, ):
        return self.driver.find_element(appium.webdriver.common.appiumby.AppiumBy.ANDROID_UIAUTOMATOR, locator)

    def scroll(self):
        var = self.driver.swipe

    def press_back(self):
        self.driver.back()

    def tap_x_y(self, x, y):
        self.driver.tap([(x, y)])

    def sleep(self, duration):
        time.sleep(duration)

    def get_date_string(self, date_):
        #date_elements = self.find_element_by_xpath(f'//android.view.View[@content-desc="{date}"]').click()

        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        formatted_date = f'{get_weekday_string(date_.weekday())}, {date_.strftime("%d %B %Y")}'
        print(formatted_date)
        return formatted_date
