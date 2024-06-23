import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_from_page_object import AddressSubPage
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_from_page_object import OrderSubmissionFromPage
from pages.order_submission_from_page_object import SearchByCityModal
from pages.order_submission_special_requirements_page_object import OrderSubmissionSpecialRequirementsPage
from pages.order_submission_special_requirements_page_object import KindOfTransportModal
from pages.order_submission_special_requirements_page_object import RampHeightModal
from pages.order_submission_special_requirements_page_object import HeightLimitModal


@pytest.mark.smoke
def test_order_submission_special_requirements(driver):
    address_to_search = "1-й Сельскохозяйственный проезд, д 3"
    test_city = 'Москва'

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.from_.click()

    order_submission_from_page_object = OrderSubmissionFromPage(driver)
    order_submission_from_page_object.click_search_by_city_button()

    search_by_city_modal = SearchByCityModal(driver)
    search_by_city_modal.send_city(test_city)
    city_entity = search_by_city_modal.get_valid_city_entity(test_city)
    city_entity.click()

    order_submission_from_page_object.click_address_button()

    address_sub_page_object = AddressSubPage(driver)
    address_sub_page_object.click_search_by_street_button()

    search_by_street_modal = SearchByStreetModal(driver)
    search_by_street_modal.send_street(address_to_search)
    street_entity = search_by_street_modal.get_valid_street_entity(address_to_search)
    street_entity.click()

    order_submission_from_page_object.click_save_button()

    order_submission_page_object.initialize_additional_fields()
    order_submission_page_object.click_special_requirements_and_transport_()

    order_submission_special_requirements_page_object = OrderSubmissionSpecialRequirementsPage(driver)
    order_submission_special_requirements_page_object.click_kind_of_transport()

    kind_of_transport_modal = KindOfTransportModal(driver)
    kind_of_transport_modal.click_top_loading_option()
    kind_of_transport_modal.click_save_button()

    assert (order_submission_special_requirements_page_object.kind_of_transport.get_attribute('content-desc')
            == 'Вид транспорта\nВерхняя загрузка')

    #MyToDo after each click to switch there should have been a check, but there are no suitable attributes
    order_submission_special_requirements_page_object.click_dedicated_car_switch()
    order_submission_special_requirements_page_object.click_sanitary_passport_switch()
    order_submission_special_requirements_page_object.click_medical_book_switch()
    order_submission_special_requirements_page_object.click_rear_loading_machine_switch()
    order_submission_special_requirements_page_object.click_pallets_switch()
    order_submission_special_requirements_page_object.click_fastening_straps_switch()
    order_submission_special_requirements_page_object.click_the_driver_wears_closed_clothing_switch()
    order_submission_special_requirements_page_object.click_reflective_vest_switch()
    order_submission_special_requirements_page_object.click_the_driver_has_a_russian_passport()
    order_submission_special_requirements_page_object.click_ramp_height()

    ramp_height_modal = RampHeightModal(driver)
    assert ramp_height_modal.default_option.get_attribute('checked') == 'true'
    ramp_height_modal.click_ramp_height_110_cm_option()
    assert ramp_height_modal.ramp_height_110_cm_option.get_attribute('checked') == 'true'
    ramp_height_modal.click_ramp_height_120_cm_option()
    assert ramp_height_modal.ramp_height_120_cm_option.get_attribute('checked') == 'true'
    ramp_height_modal.click_ramp_height_130_cm_option()
    assert ramp_height_modal.ramp_height_130_cm_option.get_attribute('checked') == 'true'
    ramp_height_modal.click_save_button()

    assert (order_submission_special_requirements_page_object.ramp_height.get_attribute('content-desc') ==
            'Высота пандуса\nВысота пандуса 130 см')

    order_submission_special_requirements_page_object.click_height_limit()

    height_limit_modal = HeightLimitModal(driver)
    assert height_limit_modal.default_option.get_attribute('checked') == 'true'

    height_limit_modal.click_height_limit_2_0_m()
    assert height_limit_modal.height_limit_2_0_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_height_limit_2_1_m()
    assert height_limit_modal.height_limit_2_1_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_height_limit_2_2_m()
    assert height_limit_modal.height_limit_2_2_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_height_limit_2_3_m()
    assert height_limit_modal.height_limit_2_3_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_height_limit_2_4_m()
    assert height_limit_modal.height_limit_2_4_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_height_limit_2_5_m()
    assert height_limit_modal.height_limit_2_5_m_option.get_attribute('checked') == 'true'
    height_limit_modal.click_save_button()

    assert (order_submission_special_requirements_page_object.height_limit.get_attribute('content-desc') ==
            'Ограничение по высоте\nОграничение по высоте 2.5 м')

    order_submission_special_requirements_page_object.click_save_button()

    order_submission_page_object.initialize_additional_fields()
    assert (order_submission_page_object.special_requirements_and_transport_.get_attribute('content-desc') ==
            "Спец. требования и транспорт\nВерхняя загрузка\nВысота пандуса 130 см\nОграничение по высоте 2.5 "
            "м\nВыделенная машина\nСанитарный паспорт\nМедицинская книжка\nМашина с задней загрузкой (без "
            "гидроборта)\nПаллеты\nКрепёжные ремни\nЗакрытая одежда у водителя\nСветоотражающий жилет\nПаспорт РФ у "
            "водителя")









