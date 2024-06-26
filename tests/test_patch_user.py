import allure
import requests
import data
import urls
from conftest import user_creating


class TestPatchUser:
    @allure.title('Проверка изменения данных авторизованного пользователя')
    @allure.description('Проверка успешного изменения данных, статус-кода и текста ответа')
    def test_patch_authorized_user(self, user_creating):
        user = user_creating
        token = user.json()['accessToken']
        changed_data = requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT,
                                      data=data.PatchUser.USER_PATCH_BODY,
                                      headers={'Authorization': token})
        requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': token})

        assert changed_data.status_code == 200 and changed_data.json()['success'] is True

    @allure.title('Проверка изменения данных НЕавторизованного пользователя')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_patch_unauthorized_user(self):
        unauthorized_user = requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT,
                                           data=data.TestLoginData.USER_SIGNIN_BODY)

        assert (unauthorized_user.status_code == 401 and
                unauthorized_user.json()["message"] == data.ResponseMassage.UNAUTHORIZED_USER)
