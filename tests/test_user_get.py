from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(
            self):  # Тест для проверки зарегистрированноого пользователя, без передачи токена
        response = MyRequests.get('/user/2')  # Заменено функцией из My_Requeste
        Assertions.assert_id_in_content(response, 'username')
        Assertions.assert_not_id_in_content(response, 'email')
        Assertions.assert_not_id_in_content(response, 'firstName')
        Assertions.assert_not_id_in_content(response, 'lastName')

    def test_get_user_details_auth_as_same_user(
            self):  # Тест для проверки зарегистрированноого пользователя, после передачи токена

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post('/user/login', data=data)  # Заменено функцией из My_Requeste
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.get(f'/user/{user_id_from_auth_method}',  # Заменено функцией из My_Requeste
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})
        print(response2.text)

        Assertions.assert_id_in_content(response2, 'username')
        Assertions.assert_id_in_content(response2, 'email')
        Assertions.assert_id_in_content(response2, 'firstName')
        Assertions.assert_id_in_content(response2, 'lastName')

#     def test_get_user_details_auth_not_auth_id(self):             # Тест для проверки авторизации с одного аккаунта и запроса другого
#
#         data = {
#             'email': 'vinkotov@example.com',
#             'password': '1234'
#         }
#
#         response1 = MyRequests.post('/user/login', data=data)       # Заменено функцией из My_Requeste
#         auth_sid = self.get_cookie(response1, 'auth_sid')
#         token = self.get_header(response1, 'x-csrf-token')
#         user_id_from_auth_metod = self.get_json_value(response1, 'user_id')
#
#         response2 = MyRequests.get(f'/user/58432', # Заменено функцией из My_Requeste
# )
#         print(response2.text)
#
#         # Assertions.assert_id_in_content(response2, 'username')
#         Assertions.assert_not_id_in_content(response2, 'email')
#         Assertions.assert_not_id_in_content(response2, 'firstName')
#         Assertions.assert_not_id_in_content(response2, 'lastName')
