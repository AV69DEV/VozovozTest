import pytest
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_date_page_object import OrderSubmissionDatePage
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
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
    order_submission_page_object.press_back()
