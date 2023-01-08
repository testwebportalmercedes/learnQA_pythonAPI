from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    def test_cannot_delete_id2(self):                                                          # Тест на попытку удолить пользователя по ID 2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }


        response1 = MyRequests.post('/user/login', data=data)


        self.user_id_from_auth_metod = self.get_json_value(response1, 'user_id')
        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')

        response2 = MyRequests.delete(f'/user/{self.user_id_from_auth_metod}',                                                                                                  # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token': self.token},
                                 cookies={'auth_sid': self.auth_sid}
                                 )
        Assertions.assert_not_text_in_response(response2, 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.')

        print(response2.text)

    def test_can_delete_accaunt_after_register_and_auth(self):
        # Register
        data = self.test_user_register()
        response1 = MyRequests.post('/user',data=data)

        Assertions.assert_code_status(response1,200)
        Assertions.assert_id_in_content(response1,'id')

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
        self.user_id_from_auth_metod = self.get_json_value(response2, 'user_id')
        print(self.user_id_from_auth_metod)

        # Delete

        response3 = MyRequests.delete(f'/user/{self.user_id_from_auth_metod}',                                                                                                  # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid}
                                 )

        # Get

        response4 = MyRequests.get(f'/user/{self.user_id_from_auth_metod}',                          # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token':token},
                                 cookies={'auth_sid':auth_sid})

        Assertions.assert_not_text_in_response(response4, 'User not found')
        print(response4.text)