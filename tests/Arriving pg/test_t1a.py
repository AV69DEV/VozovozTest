import pytest
from pages.arriving_where_page_object import ArrivingWherePage, SearchByCityModal, AddressSubPage, SearchByStreetModal
from pages.home_page_object import HomePage
from pages.order_submission_from_page_object import MapSubPage
from pages.order_submission_page_object import OrderSubmissionPage
from pages.arriving_page_object import ArrivingPage


@pytest.mark.smoke
def test_arriving_1(driver):
    city_to_search = 'Волгоград'
    street_to_search = 'жданова'
    building_number_to_search = '9'
    test_string = 'Test123'
    #Нажимаем на кнопку добавить заказ
    home_page_object = HomePage(driver)
    home_page_object.click_plus_button()

    #Открывается экран "Отправка" и сразу переходим на  экран "Прибытие"
    order_submission_page_object = OrderSubmissionPage(driver)
    order_submission_page_object.click_next_button()

    #Открывается экран "прибытие"
    arriving_page_object = ArrivingPage(driver)
    arriving_page_object.click_where_button()  #Клик по кнопку "Куда"

    #Открывается экран "Куда"
    arriving_where_page_object = ArrivingWherePage(driver)
    arriving_where_page_object.click_search_by_city_button()  #Кликаем на "поиск по городу"

    #Открывается модалка "поиск по городу"
    search_by_city_modal = SearchByCityModal(driver)

    search_by_city_modal.get_valid_city_entity("Москва")
    search_by_city_modal.get_valid_city_entity('Санкт-Петербург')

    #Отправляем не валидное название города
    search_by_city_modal.send_city(test_string)
    search_by_city_modal.check_if_nothing_found_banner_here()  #Проверяем, что действительно ничего не найденно и отрисовался баннер

    #Отправляем валидное название города
    search_by_city_modal.send_city(city_to_search)
    #Проверяем, что в результатах поиска есть искомый город
    city_web_element = search_by_city_modal.get_valid_city_entity(city_to_search)
    city_web_element.click()  #Кликаем по названию города который искали

    #Открывается экран прибытие и в поле "поиск по городу" отображается название искомого города
    arriving_where_page_object = ArrivingWherePage(driver)  #Заного инициализируем экран тк поля поменялись
    #Проверяем что город корректно отобразился
    arriving_where_page_object.search_by_city_button.get_attribute('content-desc').__contains__(
        f'{city_to_search}\nПоиск по городу')

    #Кликаем на раздел "Адрес"
    arriving_where_page_object.click_address_button()
    #Открывается раздел адрес
    address_sub_page_obj = AddressSubPage(driver)
    #Кликаем по кнопке поиск по городу
    address_sub_page_obj.click_search_by_street_button()
    #Открывается модалка поиск по городу
    search_by_street_modal = SearchByStreetModal(driver)
    #Вводим любую строку по которой не ожидаем результатов поиска
    search_by_street_modal.send_street(test_string)

    #проверяем что появился элемент с предупреждением о выборе адреса вручную и кликаем по нему
    search_by_street_modal.clik_select_address_manually()
    #Возвращаемся в раздел "Адрес" и проверяем что адрес который мы вводили корректно записался
    address_sub_page_obj.search_by_street_button.get_attribute('content-desc').__contains__(test_string)

    #Кликаем по кнопке поиск по городу
    address_sub_page_obj.click_search_by_street_button(test_string)
    #Открывается модалка поиск по городу
    search_by_street_modal = SearchByStreetModal(driver)
    #Вводим существующий адрес
    search_by_street_modal.send_street(f'{street_to_search} {building_number_to_search}')
    #Проверяем, что в списке резутатов поиска есть нужный адрес и кликаем по нему
    existing_address = search_by_street_modal.get_valid_street_entity(street=street_to_search,
                                                                      building_number=building_number_to_search)
    existing_address.click()

    #Открывается раздел "Адрес" и проверяем что адрес верно отобразился
    address_sub_page_obj.search_by_street_button.get_attribute('content-desc').casefold().__contains__(
        f"{street_to_search}" and f"{building_number_to_search}")
    #Кликаем на иконку карты
    address_sub_page_obj.click_map_button()
    #Открывается модалка, проверяем что необходимые элементы подгрузились в момент инициализации и закрываем модалку
    map_sub_page = MapSubPage(driver)
    map_sub_page.press_back()

    #Открывается раздел "Адрес" на экране "Куда", кликаем сохранить
    arriving_where_page_object.click_save_button()
    #Открывается экран "Прибытие", проверяем что появились все дополнительные поля инициализируя их
    arriving_page_object.initialize_additional_fields()
    #Проверяем, что в поле "Куда" отобразился верный адрес
    arriving_page_object.where_.get_attribute('content-desc').casefold().__contains__(
        f"{street_to_search}" and f"{building_number_to_search}")

