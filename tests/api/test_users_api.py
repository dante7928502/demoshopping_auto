import pytest
import allure


@allure.epic("API")
@allure.feature("Users")
class TestUsersAPI:

    @allure.story("Create user via API, then verify in DB and via API")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self, api_client, db_cursor, random_login, random_password):
        """Тест создания пользователя через API, проверка в БД и через API"""
        username = random_login
        password = random_password
        user_data = {"username": username, "password": password}

        with allure.step("Отправка POST запроса на создание пользователя"):
            response = api_client.post("/register", json=user_data)
            assert (
                response.status_code == 200
            ), f"Expected 200, got {response.status_code}"

        with allure.step("Проверка, что пользователь создан в БД"):
            db_cursor.execute("SELECT * FROM users WHERE login = %s", (username,))
            user_in_db = db_cursor.fetchone()
            assert user_in_db is not None, "User not found in DB"
            assert (
                user_in_db["password"] == user_data["password"]
            ), "Passwords not match"

        with allure.step("Проверка, что пользователя отображает через API"):
            response = api_client.get("/users")
            assert response.status_code == 200

            users = response.json()
            for user in reversed(users):
                if user["user_id"] == user_in_db["user_id"]:
                    assert (
                        user["login"] == user_in_db["login"]
                    ), "Logins from DB and API does not match for same user_id"


    @allure.story("Get user by ID (existing user)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_existing_user(self, api_client, existing_test_user):
        """
        Тест получения пользователя, который уже существует в БД.
        Используем фикстуру existing_test_user, чтобы получить ID и login существующей записи.
        """
        with allure.step(f"Запрос GET /users"):
            response = api_client.get("/users")
            assert response.status_code == 200

            users = response.json()
            for user in users:
                if user["user_id"] == existing_test_user["user_id"]:
                    user_login = user["login"]
                    break

            assert (
                user_login == existing_test_user["login"]
            ), "Logins from DB and API are not match for same user_id"
