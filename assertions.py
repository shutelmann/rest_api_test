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
