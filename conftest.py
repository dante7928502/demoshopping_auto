import pytest
import os
from dotenv import load_dotenv
from db.connection import DBConnection
from api.client import APIClient
from tests.utils.data_gen import generate_login, generate_password
from selenium import webdriver

load_dotenv()


@pytest.fixture(scope="session")
def db_connection():
    """Фикстура для подключения к БД на уровне сессии"""
    with DBConnection() as conn:
        yield conn


@pytest.fixture
def db_cursor(db_connection):
    """Фикстура для курсора (только чтение). Транзакции не используются."""
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    return APIClient()


@pytest.fixture
def existing_test_user(db_cursor):
    """
    Фикстура, возвращающая данные существующего тестового пользователя из БД.
    Предполагается, что в БД есть пользователь с известным email или мы берём первого попавшегося.
    """
    # Например, ищем пользователя с тестовым email
    login = os.getenv("TEST_USER_LOGIN")
    db_cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
    user = db_cursor.fetchone()
    if not user:
        # Если нет, берём первого пользователя (для демонстрации)
        db_cursor.execute("SELECT * FROM users LIMIT 1")
        user = db_cursor.fetchone()
        if not user:
            pytest.skip("No test users found in database")
    return user


@pytest.fixture
def auth_api_client(api_client, existing_test_user):
    """
    Фикстура для авторизованного клиента.
    Используем существующего пользователя для получения токена через API логина.
    Не создаём нового пользователя в БД.
    """
    
    login_data = {
        "username": existing_test_user["login"],
        "password": os.getenv("TEST_USER_PASSWORD"),
    }
    response = api_client.post("/login", json=login_data)
    assert response.status_code == 200, "Login failed for test user"
    token = response.json().get("token")
    api_client.set_auth_token(token)
    return api_client


@pytest.fixture(scope="session")
def random_login():
    return generate_login()


@pytest.fixture(scope="session")
def random_password():
    return generate_password()
