import requests
import pprint

# Отправляем GET-запрос к API JSONPlaceholder с параметром userId=1
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1
}

response = requests.get(url, params=params)

# Распечатываем полученные записи
if response.status_code == 200:
    posts = response.json()
    pprint.pprint(posts)
else:
    print("Ошибка при получении данных:", response.status_code)