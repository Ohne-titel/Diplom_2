class TestLoginData:
    USER_SIGNIN_BODY = {
        "email": "miagkova.elina@yandex.ru",
        "password": "123456",
        "name": "Элина"
    }


class IncompleteTestSignInData:
    EMAIL_AND_PASSWORD = {
        "email": "miagkova.elina@yandex.ru",
        "password": "123456"
    }


class ResponseMassage:
    USER_EXIST_MASSAGE = "User already exists"
    REQUIRED_FIELD_MASSAGE = "Email, password and name are required fields"
    INCORRECT_EMAIL_AND_PASSWORD = "email or password are incorrect"
    EXISTED_EMAIL = "User with such email already exists"
    UNAUTHORIZED_USER = "You should be authorised"
    EMPTY_INGREDIENTS = "Ingredient ids must be provided"


class PatchUser:
    USER_PATCH_BODY = {
        "email": "test@yandex.com",
        "password": "1234567",
        "name": "Лина"
    }


class OrderData:
    INGREDIENTS_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6c"]
    }

    EMPTY_ORDER = {"ingredients": ""}

    WRONG_HASH = {
        "ingredients": ["60d3b41abdacab0a733c6", "609646e4dc70"]
    }
