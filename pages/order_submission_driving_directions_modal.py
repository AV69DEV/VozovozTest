import sys

from pages.base_page import BasePage
from appium.webdriver.errorhandler import sel_exceptions


class Exceptions(Exception):
    def __init__(self):
        super().__init__()


class OrderSubmissionDrivingDirectionsModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.load_file_button = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Загрузить"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')
        self.file_loaded_banner = None
        self.file_deleted_banner = None
        self.loaded_file = None
        self.delete_loaded_file = None
        self.load_new_file = None
        self.download_file = None

    def click_load_file_button(self):
        self.load_file_button = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Загрузить"]')
        self.load_file_button.click()

    def check_loaded_file(self, file_name):
        self.loaded_file = self.find_element_by_xpath(f'//*[contains(@content-desc,"{file_name}")]')

    def click_delete_loaded_file(self):
        self.delete_loaded_file.click()

    def click_load_new_file(self):
        self.load_new_file.click()

    def click_download_file(self):
        self.download_file.click()

    def click_save_button(self):
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')
        self.save_button.click()

    def check_download_link(self):
        try:
            google_chrome_terms_of_service_page = self.find_element_by_xpath(
                '//android.widget.Button[@resource-id="com.android.chrome:id/terms_accept"]')
            google_chrome_terms_of_service_page.is_displayed()
            google_chrome_terms_of_service_page.click()

        except Exceptions:
            print(sys.exc_info())

        try:
            google_chrome_sign_in_sync_title = self.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.android.chrome:id/signin_sync_title"]')
            google_chrome_sign_in_sync_title.is_displayed()
            sync_negative_button = self.find_element_by_xpath(
                '//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]')
            sync_negative_button.is_displayed()
            sync_negative_button.click()

        except Exceptions:
            print(sys.exc_info())

        try:
            notifications_banner = self.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.android.chrome:id/notification_permission_rationale_title"]')
            notifications_banner.is_displayed()
            notifications_negative_button = self.find_element_by_xpath(
                '//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]')
            notifications_negative_button.is_displayed()
            notifications_negative_button.click()

        except Exceptions:
            print(sys.exc_info())

        url_bar = self.find_element_by_xpath('//android.widget.EditText[@resource-id="com.android.chrome:id/url_bar"]')
        return url_bar.get_attribute('text').__contains__('vozovoz.dev/upload/roadmap/')

    def init_loaded_file_additional_fields(self):
        self.delete_loaded_file = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Удалить"]')
        self.load_new_file = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Загрузить новый файл"]')
        self.download_file = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Скачать"]')

    def file_loaded_banner_displayed(self):
        try:
            self.file_loaded_banner = self.find_element_by_xpath('//android.view.View[@content-desc="Файл загружен"]',
                                                                 timeout=3)

        except sel_exceptions.StaleElementReferenceException:
            print('StaleElementException occurred!')
            return False
        except sel_exceptions.TimeoutException:
            print('TimeoutException occurred!')
            return False

        return self.file_loaded_banner.is_displayed()

    def file_deleted_banner_displayed(self):
        try:
            self.file_deleted_banner = self.find_element_by_xpath('//android.view.View[@content-desc="Файл удален"]',
                                                                  timeout=3)

        except sel_exceptions.StaleElementReferenceException:
            print('StaleElementException occurred!')
            return False
        except sel_exceptions.TimeoutException:
            print('TimeoutException occurred!')
            return False

        return self.file_deleted_banner.is_displayed()


class FileSelectionOptionModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.select_from_gallery = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Выбрать из галереи"]')
        self.select_file = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Выбрать файл"]')

    def click_select_from_gallery(self):
        self.select_from_gallery = self.find_element_by_xpath(
            '//android.widget.ImageView[@content-desc="Выбрать из галереи"]')
        self.select_from_gallery.click()

    def click_select_file(self):
        self.select_file = self.find_element_by_xpath('//android.widget.ImageView[@content-desc="Выбрать файл"]')
        self.select_file.click()
