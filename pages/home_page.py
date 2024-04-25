from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.orders_layout = self.find_element_by_xpath('//android.view.View[@content-desc="Заказы"]')

    def is_presented(self):
        self.orders_layout.is_displayed()
