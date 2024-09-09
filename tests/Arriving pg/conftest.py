import os
import subprocess
import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'
emulator_path = r'C:\Users\a.volkov\AppData\Local\Android\Sdk\emulator\emulator.exe'
avd_name = 'Samsung_Galaxy_a12_API_33_API_33'
adb_path_ = r'C:\Users\a.volkov\AppData\Local\Android\Sdk\platform-tools\adb.exe'

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung Galaxy a12', )


def start_avd(emulator, avd, adb_path):
    """subprocess.Popen([r'C:\Program Files\Git\git-bash.exe', f'emulator -avd {avd}'], shell=True)"""
    #my_process = subprocess.run([r'C:\Program Files\Git\git-bash.exe', '-c', f'emulator -avd {avd}'])
    subprocess.Popen([rf'{emulator_path}', '-avd', f'{avd}'])


"""def set_env(var_name: str, path):
    if os.getenv(var_name) is None:
        os.putenv(__name=var_name, __value=path)
    print(f'Enviroment varieble {var_name}={os.getenv(var_name)}')"""


@pytest.fixture()
def driver():
    start_avd(emulator_path, avd_name, adb_path_)
    time.sleep(5)
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.update_settings(settings={'enforceXPath1': True})
    yield driver
    if driver:
        driver.quit()
    #os.system('adb devices | grep emulator | cut -f1 | while read line; do adb -s $line emu kill; done')
    subprocess.run([r'C:\Program Files\Git\git-bash.exe', '-c', 'adb devices | grep emulator | cut -f1 | while read line; do adb -s $line emu kill; done'])
