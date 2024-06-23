from pages.base_page import BasePage


class OrderSubmissionSpecialRequirementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.kind_of_transport = self.find_element_by_xpath(
            '(//android.view.View[@content-desc="Вид транспорта"])[2]')
        self.sanitary_passport_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Санитарный паспорт"]')
        self.medical_book_switch = self.find_element_by_xpath('//android.view.View[@content-desc="Медицинская книжка"]')
        self.dedicated_car_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Выделенная машина"]')
        self.rear_loading_machine_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Машина с задней загрузкой (без гидроборта)"]')
        self.pallets_switch = self.find_element_by_xpath('//android.view.View[@content-desc="Паллеты"]')
        self.fastening_straps_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Крепёжные ремни"]')
        self.the_driver_wears_closed_clothing_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Закрытая одежда у водителя"]')
        self.reflective_vest_switch = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Светоотражающий жилет"]')
        self.the_driver_has_a_Russian_passport = self.find_element_by_xpath(
            '//android.view.View[@content-desc="Паспорт РФ у водителя"]')
        self.ramp_height = self.find_element_by_xpath('//android.view.View[@content-desc="Высота пандуса"]')
        self.height_limit = self.find_element_by_xpath('//android.view.View[@content-desc="Ограничение по высоте"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_kind_of_transport(self):
        self.tap_x_y(550, 250)

    def click_dedicated_car_switch(self):
        self.dedicated_car_switch.click()

    def click_sanitary_passport_switch(self):
        self.sanitary_passport_switch.click()

    def click_medical_book_switch(self):
        self.medical_book_switch.click()

    def click_rear_loading_machine_switch(self):
        self.rear_loading_machine_switch.click()

    def click_pallets_switch(self):
        self.pallets_switch.click()

    def click_fastening_straps_switch(self):
        self.fastening_straps_switch.click()

    def click_the_driver_wears_closed_clothing_switch(self):
        self.the_driver_wears_closed_clothing_switch.click()

    def click_reflective_vest_switch(self):
        self.reflective_vest_switch.click()

    def click_the_driver_has_a_russian_passport(self):
        self.the_driver_has_a_Russian_passport.click()

    def click_ramp_height(self):
        self.ramp_height.click()

    def click_height_limit(self):
        self.height_limit = self.find_element_by_xpath('//android.view.View[@content-desc="Ограничение по высоте"]')
        self.height_limit.click()

    def click_save_button(self):
        self.save_button.click()


class KindOfTransportModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.default_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="По умолчанию"]')
        self.side_loading_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Боковая загрузка"]')
        self.top_loading_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Верхняя загрузка"]')
        self.tail_lift_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Гидроборт"]')
        self.open_car_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Открытая машина"]')
        self.canopy_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Растентовка"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_save_button(self):
        self.save_button.click()

    def click_top_loading_option(self):
        self.top_loading_option.click()


class RampHeightModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.default_option = self.find_element_by_xpath('//android.widget.RadioButton[@content-desc="По умолчанию"]')
        self.ramp_height_110_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 110 см"]')
        self.ramp_height_120_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 120 см"]')
        self.ramp_height_130_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 130 см"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_default_option(self):
        self.default_option = self.find_element_by_xpath('//android.widget.RadioButton[@content-desc="По умолчанию"]')
        self.default_option.click()

    def click_ramp_height_110_cm_option(self):
        self.ramp_height_110_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 110 см"]')
        self.ramp_height_110_cm_option.click()
        self.ramp_height_110_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 110 см"]')

    def click_ramp_height_120_cm_option(self):
        self.ramp_height_120_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 120 см"]')
        self.ramp_height_120_cm_option.click()
        self.ramp_height_120_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 120 см"]')

    def click_ramp_height_130_cm_option(self):
        self.ramp_height_130_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 130 см"]')
        self.ramp_height_130_cm_option.click()
        self.ramp_height_130_cm_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Высота пандуса 130 см"]')

    def click_save_button(self):
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')
        self.save_button.click()
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')


class HeightLimitModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.default_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="По умолчанию"]')
        self.height_limit_2_0_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2 м"]')
        self.height_limit_2_1_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.1 м"]')
        self.height_limit_2_2_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.2 м"]')
        self.height_limit_2_3_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.3 м"]')
        self.height_limit_2_4_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.4 м"]')
        self.height_limit_2_5_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.5 м"]')
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')

    def click_default_option(self):
        self.default_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="По умолчанию"]')
        self.default_option.click()

    def click_height_limit_2_0_m(self):
        self.height_limit_2_0_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2 м"]')
        self.height_limit_2_0_m_option.click()
        self.height_limit_2_0_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2 м"]')

    def click_height_limit_2_1_m(self):
        self.height_limit_2_1_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.1 м"]')
        self.height_limit_2_1_m_option.click()
        self.height_limit_2_1_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.1 м"]')

    def click_height_limit_2_2_m(self):
        self.height_limit_2_2_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.2 м"]')
        self.height_limit_2_2_m_option.click()
        self.height_limit_2_2_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.2 м"]')

    def click_height_limit_2_3_m(self):
        self.height_limit_2_3_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.3 м"]')
        self.height_limit_2_3_m_option.click()
        self.height_limit_2_3_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.3 м"]')

    def click_height_limit_2_4_m(self):
        self.height_limit_2_4_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.4 м"]')
        self.height_limit_2_4_m_option.click()
        self.height_limit_2_4_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.4 м"]')

    def click_height_limit_2_5_m(self):
        self.height_limit_2_5_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.5 м"]')
        self.height_limit_2_5_m_option.click()
        self.height_limit_2_5_m_option = self.find_element_by_xpath(
            '//android.widget.RadioButton[@content-desc="Ограничение по высоте 2.5 м"]')

    def click_save_button(self):
        self.save_button = self.find_element_by_xpath('//android.view.View[@content-desc="Сохранить"]')
        self.save_button.click()
