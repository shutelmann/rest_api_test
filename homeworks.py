import requests
from base_case import BaseCase


class TestCookie(BaseCase):
    def test_cookie(self):
        response = requests.get(
            "https://playground.learnqa.ru/api/homework_cookie"
        )
        self.get_cookie(response, "HomeWork")
