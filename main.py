import requests

payload = {
    "name": "shutelmann"
}

response = requests.get(
    "https://playground.learnqa.ru/api/hello",
    params=payload
)

print(response.text)
