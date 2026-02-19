import pymysql
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


class DBConnection:
    """Контекстный менеджер для работы с БД"""

    def __init__(self):
        self.connection = None
        self.config = {
            "host": os.getenv("DB_INTERN_HOST"),
            "port": int(os.getenv("DB_INTERN_PORT")),
            "user": os.getenv("DB_INTERN_USER"),
            "password": os.getenv("DB_INTERN_PASSWORD"),
            "database": os.getenv("DB_INTERN_NAME"),
            "charset": "utf8mb4",
            "cursorclass": pymysql.cursors.DictCursor,
        }

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self.config)
            logger.info("Connected to database")
            return self.connection
        except pymysql.Error as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def __exit__(self, exc_type, exc, tb):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")
