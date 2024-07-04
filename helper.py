import allure
from faker import Faker


class UserGenerate:
    @staticmethod
    @allure.step('Геренация юзера')
    def generate_user_with_faker():
        fake = Faker()

        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }


class LoginUserGenerate:
    @staticmethod
    @allure.step('Геренация юзера для неуспешного логина')
    def generate_fake_user():
        fake = Faker()

        return {
            "email": fake.email(),
            "password": fake.password(),
        }


