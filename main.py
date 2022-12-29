import requests
from json.decoder import JSONDecodeError

# # обработка JSON
# response = requests.get('https://playground.learnqa.ru/api/hello')
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
#
# except JSONDecodeError:
#     print("Response is not a JSON format")
#
# # Тип запроса params для get data для остальных
#
# response = requests.get('https://playground.learnqa.ru/api/check_type', params={'name': 'igor'})
# print(response.text)
#
# response = requests.post('https://playground.learnqa.ru/api/check_type', data={'name': 'igor'})
# print(response.text)
#
# # Код ответа
#
# response = requests.get('https://playground.learnqa.ru/api/get_301', allow_redirects=False)
# print(response.status_code)

# Куки

payload = {'login':'secret_login', 'password':'secret_pass'}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",data=payload)

print(dict(response1.cookies))

cookie_value = response1.cookies.get('auth_cookie')
cookie = {}
if cookie_value is not None:
    cookie.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie",cookies=cookie)

print(response2.text)
