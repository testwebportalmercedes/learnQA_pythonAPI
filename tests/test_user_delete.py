from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import time


class TestUserDelete(BaseCase):
    def test_cannot_delete_id2(self):  # Тест на попытку удалить пользователя по ID 2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post('/user/login', data=data)
        self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')
        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        response2 = MyRequests.delete(f'/user/{self.user_id_from_auth_method}',  # Заменено функцией из My_Requeste
                                      headers={'x-csrf-token': self.token},
                                      cookies={'auth_sid': self.auth_sid}
                                      )
        Assertions.assert_not_text_in_response(response2, 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.')
        print(response2.text)

    def test_can_delete_account_after_register_and_auth(self):
        # Register
        data = self.test_user_register()
        response1 = MyRequests.post('/user', data=data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_id_in_content(response1, 'id')
        email = data['email']
        firstName = data['firstName']
        password = data['password']
        user_id = self.get_json_value(response1, 'id')

        # Login
        data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Delete
        response3 = MyRequests.delete(f'/user/{user_id}',  # Заменено функцией из My_Requeste
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid}
                                      )

        # Get
        response4 = MyRequests.get(f'/user/{user_id}',
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})

        Assertions.assert_not_text_in_response(response4, 'User not found')
        print(response4.text)

    def test_cannot_delete_account(self):  # Попытка удаления аккаунта из другого аккаунта
        data1 = self.test_user_register()
        response1 = MyRequests.post('/user', data=data1)
        email1 = data1['email']
        firstName1 = data1['firstName']
        password1 = data1['password']
        user_id1 = self.get_json_value(response1, 'id')
        time.sleep(2)
        data2 = self.test_user_register()
        response2 = MyRequests.post('/user', data=data2)
        email2 = data2['email']
        firstName2 = data2['firstName']
        password2 = data2['password']
        user_id2 = self.get_json_value(response2, 'id')
        print(user_id1)
        print(user_id2)

        # Login
        data = {
            'email': email1,
            'password': password1
        }
        response3 = MyRequests.post('/user/login', data=data)
        auth_sid = self.get_cookie(response3, 'auth_sid')
        token = self.get_header(response3, 'x-csrf-token')
        user_id = self.get_json_value(response3, 'user_id')
        print(user_id)

        # Delete
        response4 = MyRequests.delete(f'/user/{user_id2}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid}
                                      )

        # Get
        response5 = MyRequests.get(f'/user/{user_id2}',
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})

        Assertions.assert_id_in_content(response5, 'username')
        print(response5.text)
