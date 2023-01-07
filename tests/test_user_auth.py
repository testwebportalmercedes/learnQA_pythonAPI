import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

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

        # response1= requests.post('https://playground.learnqa.ru/api/user/login', data=data)                                                                                # Заменено функцией из My_Requeste
        response1= MyRequests.post('/user/login', data=data)



        # assert 'auth_sid' in response1.cookies, 'There is no auth cookie in the response'
        #
        # assert 'x-csrf-token' in response1.headers, 'There is no CSRF token'                                                                                                 # Заменено функциями из base_case
        # assert 'user_id' in response1.json(), 'There is no user id'

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_auth_metod = self.get_json_value(response1, 'user_id')



        # self.auth_sid = response1.cookies.get('auth_sid') > self.auth_sid = self.get_cookie(response1, 'auth_sid')
        # self.token = response1.headers.get('x-csrf-token') > self.token = self.get_header(response1, 'x-csrf-token')                                                          # Заменено функциями из base_case
        # self.user_id_from_auth_metod = response1.json()['user_id'] > self.user_id_from_auth_metod = self.gei_json_value(response1, 'user_id')



    def test_auth_user(self):   # Позитивный тест

        response2 = MyRequests.get('/user/auth',                                                                                                  # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token': self.token},
                                 cookies={'auth_sid': self.auth_sid}
                                 )

        Assertions.assert_json_value_by_name(
            response2,
            'user_id',
            self.user_id_from_auth_metod,
            'User id from auth metod is not equal to user id from check method'
        )

        # assert "user_id" in response2.json(), 'There is no user id in second response'
        #
        # user_id_from_check_metod = response2.json()['user_id']                                                                                                              # Заменено функциями из assertions
        #
        # assert self.user_id_from_auth_metod == user_id_from_check_metod, 'Юзеры совпадают'


    @pytest.mark.parametrize('condition', exclude_paras)
    def test_negative_auth_user(self,condition):  #негативный тест
        if condition == 'no_token':
            response2 = MyRequests.get('/user/auth',                                                                                             # Заменено функцией из My_Requeste
                                     headers={'x-csrf-token' : self.token}    # Передает неверный токен и получаем в ответе ID = 0
                                     )
        else:
            response2 = MyRequests.get('/user/auth',                                                                                             # Заменено функцией из My_Requeste
                                     cookies={'auth_sid': self.auth_sid}
                                     )

        Assertions.assert_json_value_by_name(
            response2,
            'user_id',
            0,
            f'юзер id {condition}'
        )

        # assert 'user_id' in response2.json(), 'Нет юзер ID'
        # user_id_from_check_metod= response2.json()['user_id']                                                                                                              # Заменено функциями из assertions
        # assert user_id_from_check_metod ==0 , f'юзер id {condition} '
