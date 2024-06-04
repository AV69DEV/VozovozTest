from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_title = self.find_element_by_xpath('//android.view.View[@content-desc="Оформление"]')
        self.create_order_button = self.find_element_by_xpath('//android.view.View[@content-desc="Создать"]')

    def is_presented(self) -> bool:
        return self.checkout_title.is_displayed()

    def click_create_order_button(self):
        self.create_order_button.click()
