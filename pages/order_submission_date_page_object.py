import calendar
import sys
from datetime import date, timedelta
from util.Exceptions import Exceptions
from pages.base_page import BasePage


class OrderSubmissionDatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar_background = self.find_element_by_xpath(
            '//android.view.View[@resource-id="android:id/navigationBarBackground"]')
        self.forward_button = self.find_element_by_xpath('//android.widget.Button[@content-desc="Forward"]')
        ###MyTODO Change "hard code" date, to aglgoritm witch will select the nearest possible date.

    def click_forward_button(self):
        self.forward_button.click()

    def test_date(self):
        today_date = date.today()
        current_date = today_date
        current_month = current_date.month
        current_year = current_date.year
        is_valid = False
        i = 0

        while (not is_valid) and i < 10:
            try:
                month_info = calendar.monthrange(current_year, current_month)
                tomorrow = today_date + timedelta(days=1)

                if current_date.day == month_info[1]:
                    self.click_forward_button()
                    current_date = current_date + timedelta(days=1)
                    i += 1

                if current_date == tomorrow:
                    current_date = current_date + timedelta(days=1)
                    i += 1
                    continue

                current_date_element = self.find_element_by_xpath(
                    f'//*[contains(@content-desc, "{self.get_date_string(current_date)}")]')

                if current_date_element.get_attribute('content-desc').__contains__('Disabled date'):
                    current_date = current_date + timedelta(days=1)
                    i += 1
                    continue
                else:
                    is_valid = True
                    current_date_element.click()
                    return current_date

            except Exceptions:
                i += 1
                print(sys.exc_info())




