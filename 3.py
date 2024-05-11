import requests

# Создаем словарь с данными для отправки
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Отправляем POST-запрос с данными к API JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url, data=data)

# Распечатываем статус-код и содержимое ответа
print("Статус-код ответа:", response.status_code)
print("Содержимое ответа:", response.json())