# https://petstore.swagger.io/

import requests
import random
import string

# URL для POST-запроса
url = "https://petstore.swagger.io/v2/pet"

# Заголовки
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

pet_id = random.randint(700, 1000)

# Данные для POST
data = {
  "id": pet_id,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# POST-запрос
response = requests.post(url, json=data, headers=headers)

# Результат
print("Ответ сервера [POST]:", response.json())
print("Полученный ID:", response.json()["id"])
print("Статус-код:", response.status_code)

# GET-запрос
response = requests.get(f"{url}/{pet_id}", headers=headers)
print("Ответ сервера [GET]:", response.json())
print("Полученный ID:", response.json()["id"])
print("Текущее имя:", response.json()["name"])
print("Статус-код:", response.status_code)

# PUT-запрос

new_string = "".join(random.choices(string.ascii_letters, k=5))

data = {
  "id": pet_id,
  "category": {
    "id": 0,
    "name": f"{new_string}"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.put(url, json=data, headers=headers)
print("Ответ сервера [PUT] :", response.json())
print("Новое имя:", response.json()["category"]["name"])
print("Статус-код:", response.status_code)

# DELETE-запрос
response = requests.delete(f"{url}/{pet_id}", headers=headers)
print("Статус-код после удаления:", response.status_code)

# Проверка существования сущности
response = requests.get(f"{url}/{pet_id}", headers=headers)
print(f"Проверка наличия питомца {pet_id} :", response.json())
