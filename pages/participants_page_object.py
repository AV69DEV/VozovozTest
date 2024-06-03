from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class ParticipantsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sender_button = self.find_element_by_xpath('//*[contains(@content-desc,"Отправитель")]')
        self.recipient_button = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Получатель\nОтправить код для получения груза"]')
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]')
        self.back_button = self.find_element_by_xpath('//android.view.View[@content-desc="Назад"]')

    def click_next_button(self):
        self.next_button.click()

    def click_back_button(self):
        self.back_button.click()

    def click_sender_button(self):
        self.sender_button.click()

    def click_recipient_button(self):
        self.recipient_button.click()
