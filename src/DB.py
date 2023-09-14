import psycopg2

import utils

class PostgreSQLDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.connection.autocommit = True
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            #return cursor.fetchall()
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
