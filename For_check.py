# Параметризация

import requests
import pytest
class Test_Examle:
    names = [
        ('Igor'),
        ('Dmitry'),
        ('')
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello(self,name):
        url = 'https://playground.learnqa.ru/api/hello'

        data = {'name': name}

        response = requests.get(url, params= data)

        assert response.status_code == 200, 'Код ответа не совпадает'
        response_dict = response.json()
        assert 'answer' in response_dict, 'нет ответа'

        expected_response_test = f'Hello, {name}'
        actual_response_test = response_dict['answer']
        assert actual_response_test == expected_response_test, "текст не совпадает"


