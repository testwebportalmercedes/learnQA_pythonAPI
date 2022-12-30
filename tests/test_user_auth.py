import requests
import pytest
from lib.base_case import BaseCase

class TestUserAuth(BaseCase):
    exclude_paras = [
        ('no_cookie'),
        ('no_token')
    ]
    def setup(self):  # эти данные загружаются при каждом тесте
        data = {
            'email' : 'vinkotov@example.com',
            'password' : '1234'
        }

        response1= requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        print(dict(response1.cookies))


        # assert 'auth_sid' in response1.cookies, 'There is no auth cookie in the response'
        #
        # assert 'x-csrf-token' in response1.headers, 'There is no CSRF token'
        # assert 'user_id' in response1.json(), 'There is no user id'

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_auth_metod = self.get_json_value(response1, 'user_id')



        # self.auth_sid = response1.cookies.get('auth_sid') > self.auth_sid = self.get_cookie(response1, 'auth_sid')
        # self.token = response1.headers.get('x-csrf-token') > self.token = self.get_header(response1, 'x-csrf-token')
        # self.user_id_from_auth_metod = response1.json()['user_id'] > self.user_id_from_auth_metod = self.gei_json_value(response1, 'user_id')



    def test_auth_user(self):   # Позитивный тест

        response2 = requests.get('https://playground.learnqa.ru/api/user/auth',
                                 headers={'x-csrf-token': self.token},
                                 cookies={'auth_sid': self.auth_sid}
                                 )
        assert "user_id" in response2.json(), 'There is no user id in second response'

        user_id_from_check_metod = response2.json()['user_id']

        assert self.user_id_from_auth_metod == user_id_from_check_metod, 'Юзеры совпадают'


    @pytest.mark.parametrize('condition', exclude_paras)
    def test_negative_auth_user(self,condition):  #негативный тест
        if condition == 'no_token':
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth',
                                     headers={'x-csrf-token' : self.token}    # Передает неверный токен и получаем в ответе ID = 0
                                     )
        else:
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth',
                                     cookies={'auth_sid': self.auth_sid}
                                     )

        assert 'user_id' in response2.json(), 'Нет юзер ID'
        user_id_from_check_metod= response2.json()['user_id']
        assert user_id_from_check_metod ==0 , f'юзер id {condition} '
