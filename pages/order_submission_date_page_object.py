from pages.base_page import BasePage


class OrderSubmissionDatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar_background = self.find_element_by_xpath(
            '//android.view.View[@resource-id="android:id/navigationBarBackground"]')
        ###MyTODO Change "hard code" date, to aglgoritm with will select the nearest possible date.

    def test_date(self, date: str):
        self.find_element_by_xpath(f'//android.view.View[@content-desc="{date}"]').click()
