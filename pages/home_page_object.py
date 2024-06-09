from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.orders_layout = self.find_element_by_xpath('//android.view.View[@content-desc="Заказы"]')
        self.plus_button = self.find_element_by_xpath('//android.widget.Button')
        self.new_order = None

    def is_presented(self):
        self.orders_layout.is_displayed()

    def click_new_order(self):
        self.new_order = self.find_element_by_xpath('//android.view.View[@content-desc="Новый заказ"]')
        self.new_order.click()

    def click_plus_button(self):
        self.plus_button.click()


