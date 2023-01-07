
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from datetime import datetime

class TestUserRegister(BaseCase):

    # def setup(self):                                                          # Создание нового емайла по времени перенесен в класс BASE CASE
    #     base_path = 'learnqa'
    #     domain = 'example.com'
    #     random_part = datetime.now().strftime('%m%d%y%H%M%S')
    #     self.email = f'{base_path}{random_part}@{domain}'


    def test_user_successfully(self):
        data = self.test_user_register()
        # data = {                                                              # Возвращаем data из BASE CASE
        #
        #     'username': 'learnqa1',
        #     'firstName': 'learnqa1',
        #     'lastName': 'learnqa1',
        #     'email': self.email,
        #     'password': '123'
        # }
        response = MyRequests.post('/user/', data=data)                                      # Заменено функцией из My_Requeste
        Assertions.assert_id_in_content(response, 'id')                                      # функция проверки вхождения
        Assertions.assert_code_status(response, 200)                                         # функция проверки статус кода





    def test_create_user_with_existing_email(self):                            # Негативный тест что юзер уже был создан ранее
        email = 'vinkotov+2@example.com'
        data = self.test_user_register(email)                                        # Возвращаем data из BASE CASE но передаем наш емаил
        # data = {
        #
        #     'username': 'learnqa1',
        #     'firstName': 'learnqa1',
        #     'lastName': 'learnqa1',
        #     'email': email,
        #     'password': '123'
        # }

        response = MyRequests.post('/user/', data=data)                                       # Заменено функцией из My_Requeste
        Assertions.assert_code_status(response, 400)                                          # функция проверки статус кода
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f'Unexpected response content{response.content}'


