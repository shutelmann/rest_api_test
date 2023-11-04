from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    def test_create_new_user(self):
        data = self.prepare_registration_data()

        response = MyRequests.post(
            "user",
            data=data
        )

        Assertions.assert_code_status(response, 200)
        Assertions.assert_has_json_key(response, "id")

    def test_user_with_exsiting_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post(
            "user",
            data=data
        )

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Неожиданный ответ сервера: {response.content}"
