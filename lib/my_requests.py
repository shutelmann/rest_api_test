import requests


class MyRequests:
    @staticmethod
    def get(uri: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(uri, data, headers, cookies, method="GET")

    @staticmethod
    def post(uri: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(uri, data, headers, cookies, method="POST")

    @staticmethod
    def put(uri: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(uri, data, headers, cookies, method="PUT")

    @staticmethod
    def delete(uri: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(uri, data, headers, cookies, method="DELETE")

    @staticmethod
    def _send(uri: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"https://playground.learnqa.ru/api/{uri}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(
                url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(
                url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(
                url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(
                url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP-method '{method}' was recieved")

        return response
