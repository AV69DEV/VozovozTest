import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='pixel_3a', )

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_login(self) -> None:
        app = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Возовоз')
        app.click()
        # Логинимся по email
        wait.WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@text='Телефон или Email*']")))
        login_form = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Телефон или Email*']")
        login_form.click()
        login_form.send_keys('av69.dev@gmail.com')
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Далее').click()

        # Вводим пароль
        wait.WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@text='Пароль']")))
        password_form = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Пароль']")
        password_form.click()
        password_form.send_keys('91929192')
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Войти').click()


if __name__ == '__main__':
    unittest.main()
