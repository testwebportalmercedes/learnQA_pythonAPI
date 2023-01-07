import json.decoder
from datetime import datetime
from requests import Response
class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'Cannot find cookie with name {cookie_name} in the last response'
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f'Cannot find headers with name {headers_name} in the last response'
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON Format. Response text is "{response.test}"'

        assert name in response_as_dict, f'Response JSON doesnot have key "{name}"'

        return response_as_dict[name]

    def test_user_register(self, email=None):                                              # Общий тест на регистрацию
        if email is None:
            base_path = 'learnqa'
            domain = 'example.com'
            random_part = datetime.now().strftime('%m%d%y%H%M%S')
            email = f'{base_path}{random_part}@{domain}'

        return {

            'username': 'learnqa1',
            'firstName': 'learnqa1',
            'lastName': 'learnqa1',
            'email': email,
            'password': '123'
        }