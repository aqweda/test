import requests
from bs4 import BeautifulSoup

# URL �������� �����������
login_url = "https://example.com/login"

# ������ ��� �����������
username = "your_username"
password = "your_password"

# ������� ������
session = requests.Session()

# ���������� GET-������ �� �������� �����������, ����� �������� ����� CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.content, "html.parser")

# ������� ����� CSRF �� ��������
csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")

# ��������� ������ ��� POST-�������
data = {
    "username": username,
    "password": password,
    "csrf_token": csrf_token
}

# ���������� POST-������ ��� �����������
response = session.post(login_url, data=data)

# ���������, ������� �� ������ �����������
if response.status_code == 200 and "����� ����������" in response.text:
    print("����������� �������!")
else:
    print("������ �����������.")