import requests

request_params = ["GET", "POST", "PUT", "DELETE"]

request_methods = ["get", "post", "put", "delete"]

for m in request_methods:
    method = getattr(requests, m)
    for p in request_params:
        if m != "GET":
            response = method(
                "https://playground.learnqa.ru/ajax/api/compare_query_type",
                data={"method": p}
            )
            print(response.text)
        else:
            response = method(
                "https://playground.learnqa.ru/ajax/api/compare_query_type",
                params={"method": p}
            )
            print(response.text)
