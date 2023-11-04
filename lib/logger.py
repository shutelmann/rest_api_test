import os
import datetime
from requests import Response


class Logger:
    file_name = f"logs/log_{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.log"

    @classmethod
    def _write_log_to_file(cls, data=str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_requets(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'''
-----
Test: {testname}
Time: {str(datetime.datetime.now())}
Request method: {method}
Request URL: {url}
Request data: {data}
Request headers: {headers}
Request cookies: {cookies}\n'''
        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        headers_as_dict = dict(response.headers)
        cookies_as_dict = dict(response.cookies)
        data_to_add = f'''
Response status code: {response.status_code}
Response text: {response.text}
Response header: {headers_as_dict}
Response cookies: {cookies_as_dict}
-----\n'''
        cls._write_log_to_file(data_to_add)
