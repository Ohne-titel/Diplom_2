import allure
import pytest
import requests
import urls
from burger_api import BurgerApi
from helper import UserGenerate


@pytest.fixture(scope='function')
@allure.step('Создание уникального пользователя и его регистрация с последующим удалением')
def unique_user():
    generated_stuff = UserGenerate.generate_user_with_faker()
    response = BurgerApi.create_user(generated_stuff)
    token = response.json()['accessToken']
    requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': token})

    return response


@allure.step('Создание уникального пользователя')
@pytest.fixture(scope='function')
def user_creating():
    generated_stuff = UserGenerate.generate_user_with_faker()
    response = BurgerApi.create_user(generated_stuff)

    return response
