import allure
import requests
import data
import urls
from burger_api import BurgerApi


class TestGetOrder:
    @allure.title('Получение заказов конкретного авторизованного пользователя')
    @allure.description('Проверка успешного получения списка заказов, статус-кода и текста ответа')
    def test_get_order_list_authorized_user(self):
        user = BurgerApi.login_user(data.TestLoginData.USER_SIGNIN_BODY)
        token = user.json()['accessToken']
        order_list = requests.get(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, headers={'Authorization': token})

        assert order_list.status_code == 200 and order_list.json()['success'] is True

    @allure.title('Получение заказов НЕавторизованного пользователя')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_get_order_list_unauthorized_user(self):
        order_list = BurgerApi.get_order(self)

        assert order_list.status_code == 401 and order_list.json()['message'] == data.ResponseMassage.UNAUTHORIZED_USER