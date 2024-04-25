from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, locator: str, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, locator)),
                                                      message=f"Can't find element by locator: {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located((By.XPATH, locator)),
                                                      message=f"Can't find elements by locator: {locator}")
