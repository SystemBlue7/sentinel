import pyodbc
from contextlib import contextmanager

from config.settings import settings


class DatabaseManager:
    def __init__(self) -> None:
        self.server = settings.SQL_SERVER
        self.database = settings.SQL_DATABASE
        self.user = settings.SQL_USERNAME
        self.password = settings.SQL_PASSWORD
        self.driver = settings.SQL_DRIVER

    def _build_connection_string(self) -> str:
        return (
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.user};"
            f"PWD={self.password};"
            "TrustServerCertificate=yes;"
        )
    
    def get_connection(self) -> pyodbc.Connection:
        return pyodbc.connect(self._build_connection_string(), timeout=30)