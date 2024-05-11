import requests
import pprint

# Отправляем GET-запрос к API GitHub для поиска репозиториев с кодом HTML
url = "https://api.github.com/search/repositories"
params = {
    "q": "language:html"
}

response = requests.get(url, params=params)

# Распечатываем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Распечатываем содержимое ответа в формате JSON
response_json = response.json()
pprint.pprint(response_json)