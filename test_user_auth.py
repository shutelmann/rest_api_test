import requests
import pytest
from base_case import BaseCase


class TestUserAuth(BaseCase):
    exluded_params = [
        ("no_cookies"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=data
        )

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.csrf_token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(response1, "user_id")

    def test_user_auth(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), "В ответе от сервера нет поля user_id"
        user_id_from_check = response2.json()["user_id"]

        assert self.user_id_from_auth == user_id_from_check, "Идентификатор пользователя после авторизации и после провверки авторизации не совпадают"

    @pytest.mark.parametrize("condition", exluded_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookies":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.csrf_token},
            )

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json()
        user_id = response2.json()["user_id"]

        assert user_id == 0, "Неавторизованный пользователь прошёл проверку сервера"
