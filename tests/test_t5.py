import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_from_page_object import AddressSubPage
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_from_page_object import OrderSubmissionFromPage
from pages.order_submission_loading_work_page_object import LoadingWorkPage


@pytest.mark.smoke
def test_order_submission_loading_works(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"
    floors_quantity = 8

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
    order_submission_page_object.loading_work_.click()

    order_submission_loading_work_page_object = LoadingWorkPage(driver)
    order_submission_loading_work_page_object.send_floor(floors_quantity)

    if order_submission_loading_work_page_object.service_lift.get_attribute('checked') == 'false':
        order_submission_loading_work_page_object.click_service_lift()
        assert order_submission_loading_work_page_object.service_lift.get_attribute('checked') == 'true'
        order_submission_loading_work_page_object.click_service_lift()
        assert order_submission_loading_work_page_object.service_lift.get_attribute('checked') == 'false'
    else:
        order_submission_loading_work_page_object.click_service_lift()
        assert order_submission_loading_work_page_object.service_lift.get_attribute('checked') == 'false'
        order_submission_loading_work_page_object.click_service_lift()
        assert order_submission_loading_work_page_object.service_lift.get_attribute('checked') == 'true'

    order_submission_loading_work_page_object.click_confirm_button()
    order_submission_page_object.initialize_additional_fields()
    assert order_submission_page_object.loading_work_.get_attribute('content-desc') == f'Погрузочные работы\n{floors_quantity}'
