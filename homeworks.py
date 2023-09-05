import requests
from base_case import BaseCase


class TestCookie(BaseCase):
    def test_cookie(self):
        response = requests.get(
            "https://playground.learnqa.ru/api/homework_header"
        )
        header = self.get_header(response, "x-secret-homework-header")

        assert header == "Some secret value", f"Полученное значение не совпадает с ожидаемым"
