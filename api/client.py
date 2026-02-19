import requests
import os
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

class APIClient:
    """Клиент для взаимодействия с REST API"""

    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv('API_BASE_URL')
        self.session = requests.Session()

        # Настройка повторных попыток
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        # Заголовки по умолчанию
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def set_auth_token(self, token):
        """Установка токена авторизации"""
        self.session.headers.update({'Authorization': f'Bearer {token}'})

    def request(self, method, endpoint, **kwargs):
        """Базовый метод для запросов с логированием"""
        url = f'{self.base_url}{endpoint}'
        logger.info(f'{method} {url}')
        try:
            response = self.session.request(method, url, **kwargs)
            logger.info(f'Response status: {response.status_code}')
            return response
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)