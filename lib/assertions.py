from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_by_value(response: Response, name, expected_value, error_message):
        try:
            json_to_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ от сервера не является JSON файлом.\n'{response.text}'"
        assert name in json_to_dict, f"В JSON файле нет поля с названием '{name}'"
        assert json_to_dict[name] == expected_value, error_message

    @staticmethod
    def assert_has_json_key(response: Response, name):
        try:
            json_to_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ от сервера не является JSON файлом.\n'{response.text}'"
        assert name in json_to_dict, f"В JSON файле нет поля с названием '{name}'"

    @staticmethod
    def assert_has_json_keys(response: Response, names: list):
        try:
            json_to_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ от сервера не является JSON файлом.\n'{response.text}'"

        for name in names:
            assert name in json_to_dict, f"В JSON файле нет поля с названием '{name}'"

    @staticmethod
    def assert_has_not_json_key(response: Response, name):
        try:
            json_to_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ от сервера не является JSON файлом.\n'{response.text}'"
        assert name not in json_to_dict, f"В JSON файле нет поля с названием '{name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"
