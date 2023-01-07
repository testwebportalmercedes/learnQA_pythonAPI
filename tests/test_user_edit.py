
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):                                                                  # Регистрация пользователя
        # Register
        data = self.test_user_register()
        response1 = MyRequests.post('/user',data=data)                       # Заменено функцией из My_Requeste

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

        response2 = MyRequests.post('/user/login', data=data)                 # Заменено функцией из My_Requeste

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = 'Changet name'

        response3 = MyRequests.put(f'/user/{user_id}',                         # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token':token},
                                 cookies={'auth_sid':auth_sid},
                                 data={'firstName':new_name})
        Assertions.assert_code_status(response3,200)


        # Get

        response4 = MyRequests.get(f'/user/{user_id}',                          # Заменено функцией из My_Requeste
                                 headers={'x-csrf-token':token},
                                 cookies={'auth_sid':auth_sid})

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, 'Wrong name of the user after edit')


