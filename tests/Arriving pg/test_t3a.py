import pytest

from pages.arriving_page_object import ArrivingPage
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.arriving_where_page_object import AddressSubPage, ArrivingWherePage
from pages.arriving_where_page_object import SearchByStreetModal
from pages.order_submission_pick_up_time_modal import OrderSubmissionTimeModal
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
def test_time_in_arriving_page(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"

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
    arriving_page_obj.time_.click()

    order_submission_pick_up_time_modal = OrderSubmissionTimeModal(driver)
    current_from_time = order_submission_pick_up_time_modal.from_time_seek_bar.get_attribute('content-desc')
    current_to_time = order_submission_pick_up_time_modal.to_time_seek_bar.get_attribute('content-desc')

    if current_from_time == current_to_time:
        order_submission_pick_up_time_modal.scroll_from_time_seek_bar_to(True, 1, sleep_time=1)
        #in this case we can only scroll from_time_seek_bar, to_time_seek_bar scrolls automatically

        SETED_FROM_TIME = order_submission_pick_up_time_modal.from_time_seek_bar.get_attribute('content-desc')
        SETED_TO_TIME = order_submission_pick_up_time_modal.to_time_seek_bar.get_attribute('content-desc')
        order_submission_pick_up_time_modal.click_select_button()

        assert SETED_FROM_TIME == SETED_TO_TIME
        assert arriving_page_obj.time_.get_attribute('content-desc') == f"Время\n{SETED_FROM_TIME}"

    else:
        SETED_FROM_TIME = order_submission_pick_up_time_modal.from_time_seek_bar.get_attribute('content-desc')
        SETED_TO_TIME = order_submission_pick_up_time_modal.to_time_seek_bar.get_attribute('content-desc')

        while SETED_FROM_TIME != SETED_TO_TIME:
            order_submission_pick_up_time_modal.scroll_to_time_seek_bar_to(False, 1)
            order_submission_pick_up_time_modal.scroll_from_time_seek_bar_to(True, 1)

            SETED_FROM_TIME = order_submission_pick_up_time_modal.from_time_seek_bar.get_attribute('content-desc')
            SETED_TO_TIME = order_submission_pick_up_time_modal.to_time_seek_bar.get_attribute('content-desc')

        order_submission_pick_up_time_modal.sleep(1)
        order_submission_pick_up_time_modal.click_select_button()

        assert arriving_page_obj.time_.get_attribute(
            'content-desc') == f"Время\n{SETED_FROM_TIME}"

    arriving_page_obj.time_.click()

    order_submission_pick_up_time_modal.click_fixed_time(5)
    order_submission_pick_up_time_modal.scroll_to_time_seek_bar_to(False, 1)
    order_submission_pick_up_time_modal.scroll_from_time_seek_bar_to(True, 1, sleep_time=1)

    SETED_FROM_TIME = order_submission_pick_up_time_modal.from_time_seek_bar.get_attribute('content-desc')
    SETED_TO_TIME = order_submission_pick_up_time_modal.to_time_seek_bar.get_attribute('content-desc')
    order_submission_pick_up_time_modal.click_select_button()

    assert arriving_page_obj.time_.get_attribute(
        'content-desc') == f"Время\nс {SETED_FROM_TIME} до {SETED_TO_TIME}"
