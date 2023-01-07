import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):                                                                  # Регистрация пользователя
        # Register
        data = self.test_user_register()
        response1 = requests.post('https://playground.learnqa.ru/api/user',data=data)

        Assertions.assert_code_status(response1,200)
        Assertions.assert_id_in_content(response1,'id')

        email = data['email']
        firstName = data['firstName']
        password = data['password']
        user_id = self.get_json_value(response1, 'id')


        # Login                                                                                              # Логин для получения токенов
        data = {
            'email': email,
            'password': password
        }

        response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = 'Changet name'

        response3 = requests.put(f'https://playground.learnqa.ru/api/user/{user_id}',headers={'x-csrf-token':token}, cookies={'auth_sid':auth_sid},data={'firstName':new_name})
        Assertions.assert_code_status(response3,200)


        # Get

        response4 = requests.get(f'https://playground.learnqa.ru/api/user/{user_id}',headers={'x-csrf-token':token}, cookies={'auth_sid':auth_sid})

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, 'Wrong name of the user after edit')


