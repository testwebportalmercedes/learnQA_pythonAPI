import datetime
import os
from requests import Response

class Logger:
    file_name = f'logs/log_'+ str(datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S"))+'.log'
    @classmethod
    def _write_log_to_file(cls, data:str):                                      #Записать логи
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
    @classmethod
    def add_request(cls, url:str, data:dict, headers:dict, cookies:dict, metod:str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test:{testname}\n'
        data_to_add += f'Tame:{str(datetime.datetime.now())}\n'
        data_to_add += f'Requests metod: {metod}\n'
        data_to_add += f'Requests URL: {url}\n'
        data_to_add += f'Requests data: {data}\n'
        data_to_add += f'Requests headers: {headers}\n'
        data_to_add += f'Requests cookies: {cookies}\n'
        data_to_add += f'\n'

        cls._write_log_to_file(data_to_add)
    @classmethod
    def add_response(cls, response:Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f'Response code: {response.status_code}\n'
        data_to_add += f'Response text: {response.text}\n'
        data_to_add += f'Response header: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += f'\n-----\n'

        cls._write_log_to_file(data_to_add)
