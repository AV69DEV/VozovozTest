import pytest
from pages.arriving_page_object import ArrivingPage
from pages.home_page_object import HomePage
from pages.order_submission_driving_directions_modal import FileSelectionOptionModal, \
    OrderSubmissionDrivingDirectionsModal
from pages.order_submission_page_object import OrderSubmissionPage
from pages.arriving_where_page_object import AddressSubPage, ArrivingWherePage
from pages.arriving_where_page_object import SearchByStreetModal
from dotenv import load_dotenv

from pages.system.android_select_file_modal import AndroidSelectFileModal

load_dotenv()


@pytest.mark.smoke
def test_comment_to_driver_in_arriving_page(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"

    test_file_name1 = 'Cat03.jpg'
    test_file_name2 = 'PNG.png'

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.click_next_button()

    arriving_page_obj = ArrivingPage(driver)
    arriving_page_obj.click_where_button()

    arriving_where_page_obj = ArrivingWherePage(driver)
    arriving_where_page_obj.click_address_button()
    address_sub_page_object = AddressSubPage(driver)
    address_sub_page_object.click_search_by_street_button()

    search_by_street_modal = SearchByStreetModal(driver)
    search_by_street_modal.send_street(address_to_search)
    search_by_street_modal.clik_select_address_manually()

    arriving_where_page_obj.click_save_button()

    arriving_page_obj.initialize_additional_fields()
    arriving_page_obj.click_diving_directions_()

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
    arriving_page_obj.initialize_additional_fields()

    assert arriving_page_obj.driving_directions_.get_attribute(
        'content-desc') == f'Схема проезда\n{test_file_name1}'






