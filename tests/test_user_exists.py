import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserExists(BaseCase):
    def test_user_exists(self):
        response = requests.get(
            "https://playground.learnqa.ru/api/user/2"
        )
        Assertions.assert_has_json_key(response, "username")
        Assertions.assert_has_not_json_key(response, "email")
        Assertions.assert_has_not_json_key(response, "lastName")
        Assertions.assert_has_not_json_key(response, "firstName")
        print(response.content)
