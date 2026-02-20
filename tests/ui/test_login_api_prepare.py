import pytest
import allure


@allure.feature("Login")
def test_login_ui_with_api_preparation(
    api_client, driver, login_page, catalog_page, random_login, random_password
):
    """
    UI тест логина, где пользователь создаётся через API,
    а затем проверяется через UI. После теста пользователь остаётся в БД.
    """
    # Создаём пользователя через API
    user_data = {
        "username": random_login,
        "password": random_password
    }
    response = api_client.post("/register", json=user_data)
    assert response.status_code == 200

    # Выполняем UI логин
    login_page.open()
    login_page.login(user_data["username"], user_data["password"])

    assert catalog_page.is_catalog_page_loaded()
