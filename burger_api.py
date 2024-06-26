import allure
import requests
import urls


class BurgerApi:

    @allure.step('Отправка запроса на создание юзера')
    def create_user(data):
        response = requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=data)
        return response

    @allure.step('Отправка запроса на логин юзера')
    def login_user(data):
        response = requests.post(urls.BASE_URL + urls.LOGIN_USER_ENDPOINT, json=data)
        return response

    @allure.step('Отправка запроса на изменение данных юзера')
    def patch_user(data):
        response = requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT, json=data)
        return response

    @allure.step('Отправка запроса на создание заказа')
    def create_order(data):
        response = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=data)
        return response

    @allure.step('Отправка запроса на получение списка заказов')
    def get_order(self):
        response = requests.get(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT)
        return response
