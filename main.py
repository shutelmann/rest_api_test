import requests
from time import sleep

response1 = requests.get(
    "https://playground.learnqa.ru/ajax/api/longtime_job"
)
json_parcing = response1.json()
token = json_parcing["token"]
time = json_parcing["seconds"]

sleep(int(time))

response2 = requests.get(
    "https://playground.learnqa.ru/ajax/api/longtime_job",
    params={"token": token}
)

json_parcing = response2.json()
status = json_parcing["status"]

if status == "Job is ready":
    print(json_parcing["result"])
