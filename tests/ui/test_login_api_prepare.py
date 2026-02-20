import pytest
import allure

@allure.feature("Login")
def test_login_ui_with_api_preparation(api_client, driver, login_page, dashboard_page):
    """
    UI тест логина, где пользователь создаётся через API,
    а затем проверяется через UI. После теста пользователь остаётся в БД.
    """
    # Создаём пользователя через API
    user_data = {}