import requests
from lib.logger import Logger

class MyRequests():
    @staticmethod
    def post (url:str,data: dict = None, headers: dict = None,cookies:dict = None):
        return MyRequests._send(url,data,headers,cookies,"POST")
    @staticmethod
    def get (url:str,data: dict = None, headers: dict = None,cookies:dict = None):
        return MyRequests._send(url, data, headers, cookies, "GET")
    @staticmethod
    def put (url:str,data: dict = None, headers: dict = None,cookies:dict = None):
        return MyRequests._send(url, data, headers, cookies, "PUT")
    @staticmethod
    def delete (url:str,data: dict = None, headers: dict = None,cookies:dict = None):
        return MyRequests._send(url, data, headers, cookies, "DELETE")




    @staticmethod
    def _send(url:str, data:dict, headers:dict, cookies:dict, metod:str):
        url = f'https://playground.learnqa.ru/api/{url}'
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url,data,headers,cookies,metod)

        if metod == 'GET':
            response = requests.get(url, params=data, headers=headers,cookies=cookies)
        elif metod == 'POST':
            response = requests.post(url, data=data, headers=headers,cookies=cookies)
        elif metod == 'PUT':
            response = requests.put(url, data=data, headers=headers,cookies=cookies)
        elif metod == 'DELETE':
            response = requests.delete(url, data=data, headers=headers,cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{metod}' was")

        Logger.add_response(response)

        return response


