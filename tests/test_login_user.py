import allure
import data
from burger_api import BurgerApi
from data import IncompleteTestSignInData
from helper import LoginUserGenerate


class TestLoginUser:
    @allure.title('Проверка успешного логина под существующим пользователем')
    @allure.description('Проверка успешного логина, статус-кода и текста ответа')
    def test_login_user_success(self):
        response = BurgerApi.login_user(IncompleteTestSignInData.EMAIL_AND_PASSWORD)

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка логина под несуществующим пользователем')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_login_fake_user(self):
        fake_user = LoginUserGenerate.generate_fake_user()
        response = BurgerApi.login_user(fake_user)

        assert (response.status_code == 401 and
                response.json()['message'] == data.ResponseMassage.INCORRECT_EMAIL_AND_PASSWORD)
