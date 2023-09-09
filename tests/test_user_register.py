import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup_method(self):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"learnqa{random_part}@example.com"

    def test_create_new_user(self):
        data = {
            "username": "learnqa",
            "password": "123",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
        }

        response = requests.post(
            "https://playground.learnqa.ru/api/user/",
            data=data
        )

        Assertions.assert_code_status(response, 200)
        Assertions.assert_has_json_key(response, "id")

    def test_user_with_exsiting_email(self):
        email = "vinkotov@example.com"
        data = {
            "username": "learnqa",
            "password": "123",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
        response = requests.post(
            "https://playground.learnqa.ru/api/user/",
            data=data
        )

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Неожиданный ответ сервера: {response.content}"
        print(f'\n{response.status_code}, \n{response.content}')
