import pytest

from pages.arriving_page_object import ArrivingPage
from pages.home_page_object import HomePage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.order_submission_date_page_object import OrderSubmissionDatePage
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
def test_date_in_arriving_page(driver):
    #Нахимаем на значек "+" на главной странице (создать заказ)
    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()
    #Открывается экран создания заказа "Откуда", сразу нажимаем кнопку "далее"
    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.click_next_button()

    #Открывается экран "Куда", нажимаем на поле "Дата"
    arriving_page_obj = ArrivingPage(driver)
    arriving_page_obj.click_date_()

    #Открывается модалка дата
    order_submission_date_page_object = OrderSubmissionDatePage(driver)

    # Алгоритм проверяет доступность дат и выбирает любую доступную кроме завтрашней и сегодняшней,
    # если дата удовлетворяющая этим условиям не найдена в текущем месяце, поиск продолжается по следующему месяцу и тд.
    set_date = order_submission_date_page_object.test_date().strftime("%d.%m.%Y")

    # клик на кнопку "выбрать" по кординатам тк нет уникальных локаторов
    order_submission_page_object.driver.tap([(360, 1490)])

    #Проверяем что выбранная дата корректно отобразилась на экране "Прибытие"
    assert (arriving_page_obj.date_.get_attribute('content-desc') ==
            f'Дата\n{set_date}')
