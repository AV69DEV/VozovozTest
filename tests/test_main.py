import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.password_page_object import PasswordPage
from pages.login_page_object import LoginPage
from pages.home_page import HomePage
from util.Sample_User import SampleUser
from dotenv import load_dotenv

load_dotenv()


def test_authorization(driver):
    app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Возовоз')
    app.click()
    user = SampleUser(os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"))

    login_page_object = LoginPage(driver)
    login_page_object.send_login(user.email)
    login_page_object.click_submit()

    password_page_object = PasswordPage(driver)
    password_page_object.send_password(user.password)
    password_page_object.click_submit()
    home_page = HomePage(driver)
    home_page.is_presented()


