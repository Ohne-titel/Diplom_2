import allure
import pytest
from burger_api import BurgerApi
from helper import UserGenerate


@allure.step('Создание уникального пользователя')
@pytest.fixture(scope='function')
def user_creating():
    generated_stuff = UserGenerate.generate_user_with_faker()
    response = BurgerApi.create_user(generated_stuff)

    return response
