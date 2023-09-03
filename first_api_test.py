import pytest
import requests


class TestAPI:
    names = [
        ("Vasya"),
        ("Petya"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_api(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {
            "name": name
        }

        response = requests.get(
            url,
            params=data
        )

        assert response.status_code == 200, "Неверный ответ сервера."

        response_dict = response.json()

        assert "answer" in response_dict, "В ответе от сервера нет поля 'answer'."

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]

        assert actual_response_text == expected_response_text, "Ожидаемый текст не соответсвует действительному."
