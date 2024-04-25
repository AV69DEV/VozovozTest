import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='pixel_3a', )


@pytest.fixture()
def driver():
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    if driver:
        driver.quit()

