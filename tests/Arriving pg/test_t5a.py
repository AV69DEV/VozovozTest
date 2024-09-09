import pytest

from pages.arriving_page_object import ArrivingPage
from pages.home_page_object import HomePage
from pages.order_submission_comment_to_driver_modal import OrderSubmissionCommentToDriverModal
from pages.order_submission_loading_work_modal import LoadingWorkModal
from pages.order_submission_page_object import OrderSubmissionPage
from pages.arriving_where_page_object import AddressSubPage, ArrivingWherePage
from pages.arriving_where_page_object import SearchByStreetModal
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
def test_comment_to_driver_in_arriving_page(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"
    test_comment = 'test123'

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
    arriving_page_obj.click_comment_to_driver_()
    order_submission_comment_to_driver_modal = OrderSubmissionCommentToDriverModal(driver)
    order_submission_comment_to_driver_modal.send_comment(test_comment)
    order_submission_comment_to_driver_modal.press_back()
    # this is necessary so that the keyboard does not obscure the point
    # at which the driver will click on the confirm button.
    order_submission_comment_to_driver_modal.click_confirm_button()

    arriving_page_obj.initialize_additional_fields()
    assert (arriving_page_obj.comment_to_driver_.get_attribute('content-desc') ==
            f'Комментарий водителю\n{test_comment}')

