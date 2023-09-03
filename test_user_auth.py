import requests
import pytest


class TestUserAuth:
    def test_user_auth(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=data
        )

        assert "auth_sid" in response1.cookies, "В ответе от сервера нет поля auth_sid"
        assert "x-csrf-token" in response1.headers, "В ответе от сервера нет заголовка с CSRF токеном"
        assert "user_id" in response1.json(), "В ответе от сервера нет поля user_id"

        auth_sid = response1.cookies.get("auth_sid")
        csrf_token = response1.headers.get("x-csrf-token")
        user_id_from_auth = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": csrf_token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response2.json(), "В ответе от сервера нет поля user_id"
        user_id_from_check = response2.json()["user_id"]

        assert user_id_from_auth == user_id_from_check, "Идентификатор пользователя после авторизации и после провверки авторизации не совпадают"

    exluded_params = [
        ("no_cookies"),
        ("no_token")
    ]

    @pytest.mark.parametrize("condition", exluded_params)
    def test_negative_auth_check(self, condition):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=data
        )

        assert "auth_sid" in response1.cookies, "В ответе от сервера нет поля auth_sid"
        assert "x-csrf-token" in response1.headers, "В ответе от сервера нет заголовка с CSRF токеном"
        assert "user_id" in response1.json(), "В ответе от сервера нет поля user_id"

        auth_sid = response1.cookies.get("auth_sid")
        csrf_token = response1.headers.get("x-csrf-token")

        if condition == "no_cookies":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": csrf_token},
            )

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response2.json()
        user_id = response2.json()["user_id"]

        assert user_id == 0, "Неавторизованный пользователь прошёл проверку сервера"
