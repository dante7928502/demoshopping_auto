import pytest
import allure
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage


@allure.feature("Login")
def test_login_ui_with_api_preparation(
    api_client, driver, random_login, random_password
):
    """
    UI тест логина, где пользователь создаётся через API,
    а затем проверяется через UI. После теста пользователь остаётся в БД.
    """
    # 1. Создаём пользователя через API
    user_data = {"username": random_login, "password": random_password}
    response = api_client.post("/register", json=user_data)
    assert response.status_code in [
        200,
        201,
    ], f"Failed to register user via API: {response.text}"

    # 2. Выполняем UI логин
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.should_be_login_page()
    login_page.login(user_data["username"], user_data["password"])

    # 3. Проверка результата
    # Создаем объект страницы, на которую должны попасть
    catalog_page = CatalogPage(driver)
    assert (
        catalog_page.is_catalog_page_loaded()
    ), "Catalog page was not loaded after login"
