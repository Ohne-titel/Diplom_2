import allure
import requests
import data
import urls
from burger_api import BurgerApi
from helper import UserGenerate


class TestCreateUser:
    @allure.title('Проверка успешного создания уникального юзера')
    @allure.description('Проверка успешного создания уникального юзера, проверка статус-кода и текста ответа')
    def test_create_unique_user_success(self):
        created_user_request = BurgerApi.create_user(UserGenerate.generate_user_with_faker())
        token = created_user_request.json()['accessToken']
        requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': token})

        assert created_user_request.status_code == 200 and created_user_request.json()['success'] is True

    @allure.title('Проверка отсутствия возможности создания двух одинаковых юзеров')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_existed_user_success(self):
        existed_user_request = BurgerApi.create_user(data.TestLoginData.USER_SIGNIN_BODY)

        assert (existed_user_request.status_code == 403 and
                existed_user_request.json()['message'] == data.ResponseMassage.USER_EXIST_MASSAGE)

    @allure.title('Проверка заполнения всех обязательных полей')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_required_fields_while_creating_user(self):
        required_field_request = BurgerApi.create_user(data.IncompleteTestSignInData.EMAIL_AND_PASSWORD)

        assert (required_field_request.status_code == 403 and
                required_field_request.json()['message'] == data.ResponseMassage.REQUIRED_FIELD_MASSAGE)