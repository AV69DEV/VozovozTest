import time
import appium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common import appiumby
from selenium.common.exceptions import StaleElementReferenceException


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
