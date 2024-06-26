from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common import appiumby
from pages.base_page import BasePage


class CargoParametrsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.next_button = self.find_element_by_xpath('//android.view.View[@content-desc="Далее"]')
        self.back_button = self.find_element_by_xpath('//android.view.View[@content-desc="Назад"]')
        self.cargo_param = self.find_element_by_xpath('//*[contains(@content-desc,"Груз")]')
        self.correspondence_param = self.find_element_by_xpath('//*[contains(@content-desc,"Корреспонденция")]')
        self.type_of_calculation_by_dimensions = self.find_element_by_xpath('//*[contains(@content-desc,"По общим '
                                                                            'габаритам")]')
        self.type_of_calculation_for_individual_places = self.find_element_by_xpath('//*[contains(@content-desc,"По '
                                                                                    'отдельным местам")]')
        self.type_of_calculation_parcel = self.find_element_by_xpath('//*[contains(@content-desc,"Посылка")]')
        self.type_of_calculation_pallet = self.find_element_by_xpath('//*[contains(@content-desc,"Паллета")]')
        self.general_dimensions = self.find_element_by_xpath('//*[contains(@content-desc,"Общие габариты")]')
        self.maximum_dimensions_of_one_place = self.find_element_by_xpath('//*[contains(@content-desc,"Максимальные '
                                                                          'габариты")]')
        self.package_param = self.find_element_by_xpath('//*[contains(@content-desc,"Упаковка")]')
        #parametrs not presented on page before scrolling are None by default
        self.cargo_categories_param = None
        self.order_price = None
        self.insurance_param = None
        self.link_transportation_number_param = None
        self.scan_of_delivery_note_param = None
        self.disassembly_of_packaging_upon_delivery_to_the_address_param = None
        self.return_accompanying_documents_param = None

    def set_initially_hidden_parameters(self):
        self.insurance_param = self.find_element_by_xpath('//*[contains(@content-desc,"Страхование")]')
        self.link_transportation_number_param = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Привязать номер перевозки")]')
        self.scan_of_delivery_note_param = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Скан накладной на выдачу")]')
        self.disassembly_of_packaging_upon_delivery_to_the_address_param = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Разбор упаковки при доставке\nдо адреса")]')
        self.return_accompanying_documents_param = self.find_element_by_xpath(
            '//*[contains(@content-desc,"Вернуть сопроводительные документы")]')
        self.cargo_categories_param = self.find_element_by_xpath('//*[contains(@content-desc,"Категория груза")]')
        self.order_price = self.find_element_by_xpath('//*[contains(@content-desc,"Сумма заказа")]')

    def click_next_button(self):
        self.next_button.click()

    def click_back_button(self):
        self.back_button.click()
