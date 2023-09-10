from requests import Response
import json
from datetime import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"В куки файлах, прикреплённых к ответу от сервера, нет поля '{cookie_name}'"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"В ответе от сервера нет заголовка с названием '{header_name}'"
        return response.headers[header_name]

    def get_json_value(self, response: Response, json_key):
        try:
            json_to_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ от сервера не является JSON файлом.\n'{response.text}'"
        assert json_key in json_to_dict, f"В ответе от сервера нет ключа с названием '{json_key}'"
        return json_to_dict[json_key]

    def prepare_registration_data(self, email=None):
        if email == None:
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"learnqa{random_part}@example.com"
        return {
            "username": "learnqa",
            "password": "1234",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
