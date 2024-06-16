import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_from_page_object import AddressSubPage
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_from_page_object import OrderSubmissionFromPage
from pages.order_submission_comment_to_driver_modal import OrderSubmissionCommentToDriverModal


@pytest.mark.smoke
def test_order_submission_comment_to_driver(driver):
    address_to_search = "пр-т. Победителей 1/2, Минск, Минская область"
    test_comment = 'test123'
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
    order_submission_page_object.click_comment_to_driver_()
    order_submission_comment_to_driver_modal = OrderSubmissionCommentToDriverModal(driver)
    order_submission_comment_to_driver_modal.send_comment(test_comment)
    order_submission_comment_to_driver_modal.press_back()
    #this is necessary so that the keyboard does not obscure the point
    # at which the driver will click on the confirm button.
    order_submission_comment_to_driver_modal.click_confirm_button()

    order_submission_page_object.initialize_additional_fields()
    assert (order_submission_page_object.comment_to_driver_.get_attribute('content-desc') ==
            f'Комментарий водителю\n{test_comment}')
