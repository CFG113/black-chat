import psycopg2
from config.config import Config

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(
                host=Config.DB_HOST,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                port=Config.DB_PORT  
            )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
