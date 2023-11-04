from lib.my_requests import MyRequests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Authorization Cases")
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

        response1 = MyRequests.post(
            "user/login",
            data=data
        )

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.csrf_token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(response1, "user_id")

    @allure.description("Это положительный тест на авторизацию.")
    def test_user_auth(self):
        response2 = MyRequests.get(
            "user/auth",
            headers={"x-csrf-token": self.csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_by_value(
            response2,
            "user_id",
            self.user_id_from_auth,
            "Идентификатор пользователя после авторизации и после провверки авторизации не совпадают"
        )

    @allure.description("Это негативный тест на авторизацию, который проверят авторизацию на сайте с помощью токена полученного в куки фалйах.")
    @pytest.mark.parametrize("condition", exluded_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookies":
            response2 = MyRequests.get(
                "user/auth",
                headers={"x-csrf-token": self.csrf_token},
            )

        response2 = MyRequests.get(
            "user/auth",
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_by_value(
            response2,
            "user_id",
            0,
            "Неавторизованный пользователь прошёл проверку сервера."
        )
