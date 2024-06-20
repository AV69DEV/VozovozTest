import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_from_page_object import AddressSubPage
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_from_page_object import OrderSubmissionFromPage
from pages.order_submission_driving_directions_modal import OrderSubmissionDrivingDirectionsModal
from pages.order_submission_driving_directions_modal import FileSelectionOptionModal
from pages.system.android_select_file_modal import AndroidSelectFileModal


@pytest.mark.smoke
def test_order_submission_driver_directions(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"
    test_file_name1 = 'Keep_it_Simple.jpg'
    test_file_name2 = 'Simple_light_bulb_graphic.png'

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.from_.click()

    order_submission_from_page_object = OrderSubmissionFromPage(driver)
    order_submission_from_page_object.click_address_button()

    address_sub_page_object = AddressSubPage(driver)
    address_sub_page_object.click_search_by_street_button()

    search_by_street_modal = SearchByStreetModal(driver)
    search_by_street_modal.send_street(address_to_search)
    search_by_street_modal.clik_select_address_manually()

    order_submission_from_page_object.click_save_button()

    order_submission_page_object.initialize_additional_fields()
    order_submission_page_object.click_diving_directions_()

    order_submission_driving_directions_modal = OrderSubmissionDrivingDirectionsModal(driver)
    order_submission_driving_directions_modal.click_load_file_button()
    file_selection_option_modal = FileSelectionOptionModal(driver)
    file_selection_option_modal.click_select_file()

    android_select_file_modal = AndroidSelectFileModal(driver)
    android_select_file_modal.get_file(test_file_name1).click()

    assert order_submission_driving_directions_modal.file_loaded_banner_displayed()
    order_submission_driving_directions_modal.tap_x_y(350, 950)
    assert not order_submission_driving_directions_modal.file_loaded_banner_displayed()

    order_submission_driving_directions_modal.check_loaded_file(test_file_name1)
    order_submission_driving_directions_modal.init_loaded_file_additional_fields()
    order_submission_driving_directions_modal.click_delete_loaded_file()

    assert order_submission_driving_directions_modal.file_deleted_banner_displayed()
    order_submission_driving_directions_modal.tap_x_y(350, 950)
    assert not order_submission_driving_directions_modal.file_deleted_banner_displayed()

    order_submission_driving_directions_modal.click_load_file_button()
    file_selection_option_modal = FileSelectionOptionModal(driver)
    file_selection_option_modal.click_select_file()
    android_select_file_modal.get_file(test_file_name2).click()

    assert order_submission_driving_directions_modal.file_loaded_banner_displayed()
    order_submission_driving_directions_modal.tap_x_y(350, 950)
    assert not order_submission_driving_directions_modal.file_loaded_banner_displayed()

    order_submission_driving_directions_modal.check_loaded_file(test_file_name2)
    order_submission_driving_directions_modal.init_loaded_file_additional_fields()

    order_submission_driving_directions_modal.click_load_new_file()
    file_selection_option_modal.click_select_file()
    android_select_file_modal.get_file(test_file_name1).click()

    assert order_submission_driving_directions_modal.file_loaded_banner_displayed()
    order_submission_driving_directions_modal.tap_x_y(350, 950)
    assert not order_submission_driving_directions_modal.file_loaded_banner_displayed()

    order_submission_driving_directions_modal.check_loaded_file(test_file_name1)
    order_submission_driving_directions_modal.init_loaded_file_additional_fields()

    order_submission_driving_directions_modal.click_download_file()
    assert order_submission_driving_directions_modal.check_download_link()
    order_submission_driving_directions_modal.press_back()

    order_submission_driving_directions_modal.click_save_button()
    order_submission_page_object.initialize_additional_fields()

    assert order_submission_page_object.driving_directions_.get_attribute('content-desc') == f'Схема проезда\n{test_file_name1}'


















