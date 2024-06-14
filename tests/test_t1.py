import os

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from util.Sample_User import SampleUser
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
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


@pytest.mark.smoke
def test_create_order(driver):
    name = "Андрей Волков"
    phone = "79157292091"
    formated_phone = "+7 (915) 729-20-91"
    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    order_submission_page_object = OrderSubmissionPage(driver)
    assert order_submission_page_object.from_.get_attribute("content-desc") == ("Откуда\nТерминал: Минск, Инженерная "
                                                                                "ул., д.4, корп. 2")
    ##assert order_submission_page_object.date_.get_attribute("content-desc") == "Дата\n22.05.2024"
    ##assert order_submission_page_object.time_.get_attribute("content-desc") == "Время\nдо 18:00"
    order_submission_page_object.click_next_button()

    arriving_page_object = ArrivingPage(driver)
    assert arriving_page_object.direction_.get_attribute("content-desc") == ("Куда\nТерминал: Санкт-Петербург, 2-ой "
                                                                             "Бадаевский проезд, 10")
    ##assert arriving_page_object.date_.get_attribute("content-desc") == "Дата\n26.05.2024"
    ##assert arriving_page_object.time_.get_attribute("content-desc") == "Время\nc 14:00"
    arriving_page_object.click_next_button()

    cargo_parametrs_page_object = CargoParametrsPage(driver)
    driver.swipe(150, 650, 150, 100, 700)
    cargo_parametrs_page_object.set_insurance_param()
    cargo_parametrs_page_object.set_link_transportation_number_param()
    cargo_parametrs_page_object.set_scan_of_delivery_note_param()
    cargo_parametrs_page_object.set_disassembly_of_packaging_upon_delivery_to_the_address_param()
    cargo_parametrs_page_object.set_return_accompanying_documents_param()
    cargo_parametrs_page_object.click_next_button()

    participants_page_object = ParticipantsPage(driver)
    participants_page_object.click_sender_button()

    sender_individuals_page_object = SenderPageIndividuals(driver)
    sender_individuals_page_object.click_name_input()

    sender_individuals_search_subpage_object = SenderIndividualsSearchSubpageObject(driver)
    sender_individuals_search_subpage_object.send_name(name)
    assert sender_individuals_search_subpage_object.check_for_valid_counterparty(name, phone)
    sender_individuals_search_subpage_object.get_valid_counterparty(name, phone).click()
    assert sender_individuals_page_object.name_input.text == f"{name} "
    assert sender_individuals_page_object.basic_phone_input.text == f"{formated_phone}"
    sender_individuals_page_object.mail_title.click()  ####Клик по элементу чтобы скрыть клавиатуру
    sender_individuals_page_object.click_save_button()

    participants_page_object.click_recipient_button()

    recipient_individuals_page_object = RecipientIndividualsPageIndividuals(driver)
    recipient_individuals_page_object.click_name_input()

    recipient_individuals_search_subpage_object = SenderIndividualsSearchSubpageObject(driver)
    recipient_individuals_search_subpage_object.send_name(name)
    assert recipient_individuals_search_subpage_object.check_for_valid_counterparty(name, phone)
    recipient_individuals_search_subpage_object.get_valid_counterparty(name, phone).click()
    assert recipient_individuals_page_object.name_input.text == f"{name} "
    assert recipient_individuals_page_object.basic_phone_input.text == f"{formated_phone}"
    recipient_individuals_page_object.mail_title.click()  ####Клик по элементу чтобы скрыть клавиатуру
    recipient_individuals_page_object.click_save_button()

    participants_page_object.click_next_button()

    checkout_page_object = CheckoutPage(driver)
    assert checkout_page_object.is_presented()
    checkout_page_object.click_create_order_button()

    order_details_page_object = OrderDetailsPage(driver)
    order_details_page_object.press_back()
