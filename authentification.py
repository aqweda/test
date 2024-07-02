import requests
from bs4 import BeautifulSoup

# URL страницы авторизации
login_url = "https://example.com/login"

# Данные для авторизации
username = "your_username"
password = "your_password"

# Создаем сессию
session = requests.Session()

# Отправляем GET-запрос на страницу авторизации, чтобы получить токен CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.content, "html.parser")

# Находим токен CSRF на странице
csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")

# Формируем данные для POST-запроса
data = {
    "username": username,
    "password": password,
    "csrf_token": csrf_token
}

# Отправляем POST-запрос для авторизации
response = session.post(login_url, data=data)

# Проверяем, успешно ли прошла авторизация
if response.status_code == 200 and "Добро пожаловать" in response.text:
    print("Авторизация успешна!")
else:
    print("Ошибка авторизации.")