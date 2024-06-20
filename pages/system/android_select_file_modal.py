from pages.base_page import BasePage


class AndroidSelectFileModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_button = self.find_element_by_xpath(
            '//android.widget.TextView[@content-desc="Search"]')

    def get_file(self, name):
        return self.find_element_by_xpath(
            f'//android.widget.TextView[@resource-id="android:id/title" and @text="{name}"]')
