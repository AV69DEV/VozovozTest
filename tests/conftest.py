import appium.webdriver.common.appiumby
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung Galaxy a12', )


@pytest.fixture()
def driver():
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.update_settings(settings={'enforceXPath1': True})
    yield driver
    if driver:
        driver.quit()
