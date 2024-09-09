import pytest
from pages.arriving_page_object import ArrivingPage
from pages.home_page_object import HomePage
from pages.order_submission_documents_address_modal import OrderSubmissionDocumentsAtTheAddressModal
from pages.order_submission_from_page_object import SearchByStreetModal
from pages.order_submission_page_object import OrderSubmissionPage
from pages.arriving_where_page_object import AddressSubPage, ArrivingWherePage, SearchByCityModal
from pages.arriving_where_page_object import SearchByStreetModal
from dotenv import load_dotenv


load_dotenv()


@pytest.mark.smoke
def test_documents_address_in_arriving_page(driver):
    address_to_search = "1-й Сельскохозяйственный проезд, д "
    building_number_to_search = "3"
    test_documents_address = "Ленина 88"
    test_city = 'Москва'

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.click_next_button()

    arriving_page_obj = ArrivingPage(driver)
    arriving_page_obj.click_where_button()

    arriving_where_page_obj = ArrivingWherePage(driver)
    arriving_where_page_obj.click_search_by_city_button()

    search_by_city_modal = SearchByCityModal(driver)
    search_by_city_modal.send_city(test_city)
    city_entity = search_by_city_modal.get_valid_city_entity(test_city)
    city_entity.click()

    arriving_where_page_obj = ArrivingWherePage(driver)
    arriving_where_page_obj.click_address_button()

    address_sub_page_object = AddressSubPage(driver)
    address_sub_page_object.click_search_by_street_button()

    search_by_street_modal = SearchByStreetModal(driver)
    search_by_street_modal.send_street(f'{address_to_search} {building_number_to_search}')
    street_entity = search_by_street_modal.get_valid_street_entity(f'{address_to_search}{building_number_to_search}')
    street_entity.click()

    arriving_where_page_obj.click_save_button()

    arriving_page_obj.initialize_additional_fields()
    arriving_page_obj.click_documents_at_the_address()

    order_submission_documents_address = OrderSubmissionDocumentsAtTheAddressModal(driver)
    order_submission_documents_address.send_address(address_to_search)
    documents_street_entity = order_submission_documents_address.get_valid_street_entity(address_to_search)
    documents_street_entity.click()

    arriving_page_obj.initialize_additional_fields()
    assert (arriving_page_obj.documents_at_the_address_.get_attribute('content-desc') ==
            f'Документы по адресу\n{address_to_search}')
