import os
import subprocess
import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'
emulator_path = '/Users/osnovnaa/library/Android/sdk/emulator/emulator'
avd_name = 'Samsung_Galaxy_a12_API_33'

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung Galaxy a12', )


def start_avd(emulator, avd):
    subprocess.Popen([f'{emulator}', '-avd', f'{avd}'])
    os.system('adb wait-for-device')


"""def set_env(var_name: str, path):
    if os.getenv(var_name) is None:
        os.putenv(__name=var_name, __value=path)
    print(f'Enviroment varieble {var_name}={os.getenv(var_name)}')"""


@pytest.fixture()
def driver():
    start_avd(emulator_path, avd_name)
    time.sleep(3)
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.update_settings(settings={'enforceXPath1': True})
    yield driver
    if driver:
        driver.quit()
    #os.system('adb devices | grep emulator | cut -f1 | while read line; do adb -s $line emu kill; done')
