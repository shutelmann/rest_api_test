from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserExists(BaseCase):
    def test_user_exists(self):
        response = MyRequests.get(
            "user/1"
        )
        Assertions.assert_has_json_keys(
            response, ["username", "email", "firstName", "lastName"])

    def test_user_with_auth(self):
        data = self.prepare_registration_data("vinkotov@example.com")
        response1 = MyRequests.post(
            "user/login",
            data=data
        )
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"user/{user_id_from_auth}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_has_json_keys(
            response2, ["username", "email", "firstName", "lastName"])
