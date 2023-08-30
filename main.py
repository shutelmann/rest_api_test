from json import JSONDecodeError
import requests

payload = {
    "name": "shutelmann"
}

response = requests.get(
    "https://playground.learnqa.ru/api/get_text",
    params=payload
)

print(response.text)

try:
    parsed_response_json = response.json()
    print(parsed_response_json["answer"])
except JSONDecodeError:
    print("Ответ сервера не содержит JSON.")
