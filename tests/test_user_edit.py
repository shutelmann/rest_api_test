import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # Register
        register_data = self.prepare_registration_data()
        response = requests.post(
            "https://playground.learnqa.ru/api/user/",
            data=register_data
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_has_json_key(response, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response, "id")

        # Login
        login_data = {
            "email": email,
            "password": password
        }

        response2 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=login_data
        )

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_name = "Changed Name"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 200)

        # Check
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_by_value(
            response4,
            "firstName",
            new_name,
            "Wrong name after user edit . . ."
        )
