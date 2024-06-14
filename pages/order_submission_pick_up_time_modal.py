import time
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class OrderSubmissionTimeModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.from_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index, "0") and contains(@class, "android.widget.SeekBar")]')
        self.to_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index, "1") and contains(@class, "android.widget.SeekBar")]')
        self.fixed_time_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Фиксированное время"]/android.view.View')
        self.select_button = self.find_element_by_xpath('//android.view.View[@content-desc="Выбрать"]')

    def click_fixed_time(self, timeout):
        self.fixed_time_switch = self.find_element_by_xpath_with_ignored_exceptions(
            '//android.view.View[@content-desc="Фиксированное время"]/android.view.View', self.ignored_exceptions)
        self.fixed_time_switch.click()

    def click_select_button(self):
        self.select_button = self.find_element_by_xpath('//android.view.View[@content-desc="Выбрать"]')
        self.select_button.click()

    def scroll_from_time_seek_bar_to(self, direction: bool, repeat=1, sleep_time=0):
        """
        !Updates from_time_seek_bar and to_time_seek_bar
        :param sleep_time:
        :param direction: when True scrolls down(from least to most), when False scrolls Up(from most to least)
        :param repeat: Int value defines how much times to repeat scroll-action, if value <= 0 trows an AssertationException
        :return: void
        """
        assert repeat > 0
        if direction:
            i = 0
            while i < repeat:
                self.driver.swipe(212, 1050, 212, 1000, 500)
                i += 1
        else:
            i = 0
            while i < repeat:
                self.driver.swipe(212, 1050, 212, 1100, 500)
                i += 1

        self.sleep(sleep_time)
        self.from_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index, "0") and contains(@class, "android.widget.SeekBar")]')
        print(f"Время забора с {self.from_time_seek_bar.get_attribute('content-desc')}")

        self.to_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index, "1") and contains(@class, "android.widget.SeekBar")]')
        print(f"До {self.to_time_seek_bar.get_attribute('content-desc')}")

    def scroll_to_time_seek_bar_to(self, direction: bool, repeat=1, sleep_time=0):
        """
        similar to scroll_from_time_bar_to function
        !Updates from_time_seek_bar and to_time_seek_bar
        :param sleep_time:
        :param direction: when True scrolls down(from least to most), when False scrolls Up(from most to least)
        :param repeat: Int value defines how much times to repeat scroll-action, if value < 0 trows an AssertationException
        :return: void
        """
        assert repeat > 0
        if direction:
            i = 0
            while i < repeat:
                self.driver.swipe(520, 1050, 520, 1000, 500)
                i += 1
        else:
            i = 0
            while i < repeat:
                self.driver.swipe(520, 1050, 520, 1100, 500)
                i += 1

        self.sleep(sleep_time)
        self.from_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index,"0") and contains(@class, "android.widget.SeekBar")]')
        print(f"Время забора с {self.from_time_seek_bar.get_attribute('content-desc')}")
        self.to_time_seek_bar = self.find_element_by_xpath(
            '//*[contains(@index,"1") and contains(@class, "android.widget.SeekBar")]')
        print(f"До {self.to_time_seek_bar.get_attribute('content-desc')}")
