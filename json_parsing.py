import json

string_as_js_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_js_format)                   # Парсим

print(obj['answer'])                                  # Обращаемся по клучу

key = 'answer'

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} нет в JSON")