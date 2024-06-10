from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_date_page_object import OrderSubmissionDatePage
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


def test_date_in_order_submission_page(driver):
    test_date_ = "чт, 27 июня 2024"
    expected_order_submission_date = 'Дата\n27.06.2024'

    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.date_.click()

    order_submission_date_page_object = OrderSubmissionDatePage(driver)
    order_submission_date_page_object.test_date(test_date_)
    order_submission_page_object.driver.tap([(360, 1490)])
    #tap to select_button corinates because there are no locators

    assert order_submission_page_object.date_.get_attribute('content-desc') == expected_order_submission_date







