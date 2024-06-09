import os
from appium.webdriver.common.appiumby import AppiumBy
from util.Sample_User import SampleUser
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.from_page_object import FromPage
from pages.from_page_object import SearchByCityModal
from pages.from_page_object import AddressSubPage
from pages.from_page_object import SearchByStreetModal
from pages.from_page_object import MapSubPage
from pages.arriving_page_object import ArrivingPage
from pages.participants_page_object import ParticipantsPage
from pages.sender_individuals_page_object import SenderPageIndividuals
from pages.sender_individuals_page_object import SenderIndividualsSearchSubpageObject
from pages.recipient_individuals_page_object import RecipientIndividualsPageIndividuals
from pages.recipient_individuals_page_object import RecipientIndividualsSearchSubpageObject
from pages.cargo_parameters_page_object import CargoParametrsPage
from pages.checkout_page_object import CheckoutPage
from pages.order_details_page_object import OrderDetailsPage
from dotenv import load_dotenv

load_dotenv()


def test_order_submission(driver):
    city_ = "Новосибирск"
    address_ = "Петухова ул. 69 В/1"
    address_to_search = "ул Ленина, д 88"
    address_to_expect = "ул Ленина, д 88\nг Новосибирск, Новосибирская обл"

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.click_from_()

    from_page_object = FromPage(driver)
    from_page_object.click_search_by_city_button()

    search_by_city_modal = SearchByCityModal(driver)
    search_by_city_modal.send_city(city_)
    valid_city = search_by_city_modal.get_valid_city_entity(city_)
    valid_city.click()

    from_page_object.check_address(address_)
    from_page_object.click_address_button()

    address_sub_page_object = AddressSubPage(driver)
    address_sub_page_object.click_search_by_street_button()

    search_by_street_modal = SearchByStreetModal(driver)
    search_by_street_modal.send_street(address_to_search)
    valid_street = search_by_street_modal.get_valid_street_entity(address_to_expect)
    valid_street.click()

    address_sub_page_object.check_displayed_street(address_to_search)
    address_sub_page_object.click_map_button()

    map_sub_page = MapSubPage(driver)
    map_sub_page.press_back()

    from_page_object.click_save_button()
    order_submission_page_object.initialize_additional_fields()
    assert order_submission_page_object.from_.get_attribute("content-desc").__contains__(
        f"Откуда\nАдрес: {city_} {address_to_search}")
