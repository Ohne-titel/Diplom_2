import allure
import requests
import data
import urls
from burger_api import BurgerApi
from data import TestLoginData, OrderData


class TestCreateOrder:
    @allure.title('Проверка создания заказа авторизованным пользователем')
    @allure.description('Проверка успешного создания заказа, статус-кода и текста ответа')
    def test_create_order_authorized_user(self):
        user = BurgerApi.login_user(TestLoginData.USER_SIGNIN_BODY)
        token = user.json()['accessToken']
        created_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, data=OrderData.INGREDIENTS_DATA,
                                      headers={'Authorization': token})

        assert created_order.status_code == 200 and created_order.json()['success'] is True

    # Тест завершается с кодом 200, согласно документации должен быть 401, здесь баг
    @allure.title('Проверка создания заказа НЕавторизованным пользователем')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_create_order_unauthorized_user(self):
        created_order = BurgerApi.create_order(OrderData.INGREDIENTS_DATA)

        assert (created_order.status_code == 401 and
                created_order.json()['message'] == data.ResponseMassage.UNAUTHORIZED_USER)

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_create_order_empty_ingredients(self):
        created_order = BurgerApi.create_order(OrderData.EMPTY_ORDER)

        assert (created_order.status_code == 400 and
                created_order.json()['message'] == data.ResponseMassage.EMPTY_INGREDIENTS)

    @allure.title('Проверка создания заказа с невалидным хешем ингредиента')
    @allure.description('Проверка ошибки, статус-кода')
    def test_create_order_wrong_hash(self):
        created_order = BurgerApi.create_order(OrderData.WRONG_HASH)

        assert created_order.status_code == 500
