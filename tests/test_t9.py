import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_from_page_object import AddressSubPage
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_from_page_object import OrderSubmissionFromPage
from pages.order_submission_from_page_object import SearchByCityModal
from pages.order_submission_documents_address_modal import OrderSubmissionDocumentsAtTheAddressModal


@pytest.mark.smoke
def test_order_submission_documents_address(driver):
    address_to_search = "1-й Сельскохозяйственный проезд, д 3"
    test_documents_address = "Ленина 88"
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
    order_submission_page_object.click_documents_at_the_address()

    order_submission_documents_address = OrderSubmissionDocumentsAtTheAddressModal(driver)
    order_submission_documents_address.send_address(address_to_search)
    documents_street_entity = order_submission_documents_address.get_valid_street_entity(address_to_search)
    documents_street_entity.click()

    order_submission_page_object.initialize_additional_fields()
    assert (order_submission_page_object.documents_at_the_address_.get_attribute('content-desc') ==
            f'Документы по адресу\n{address_to_search}')

