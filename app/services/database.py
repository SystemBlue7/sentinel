import pyodbc
from contextlib import contextmanager

from config.settings import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_USERNAME,
    SQL_PASSWORD,
    SQL_DRIVER,
)


class DatabaseManager:
    def __init__(self) -> None:
        self.server = SQL_SERVER
        self.database = SQL_DATABASE
        self.user = SQL_USERNAME
        self.password = SQL_PASSWORD
        self.driver = SQL_DRIVER

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
        conn = pyodbc.connect(self._build_connection_string(), timeout=30)
        conn.autocommit = False
        return conn

    @contextmanager
    def connect(self):
        connection = None
        try:
            connection = self.get_connection()
            yield connection
        finally:
            if connection is not None:
                connection.close()
                
    def fetch_all(self, query: str, params: tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(columns, row)) for row in rows]
    
    def fetch_one(self, query: str, params: tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()

            if row is None:
                return None

            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
    
    def execute(self, query: str, params: tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()


db = DatabaseManager()