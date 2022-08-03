import mysql.connector

from framework.singleton import Singleton


class Database(metaclass=Singleton):
    db = None

    def __init__(self, username, password, host, database=None):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def connect(self):
        if self.database is not None:
            self.db = mysql.connector.connect(user=self.username, password=self.password,
                                              host=self.host, database=self.database)
        else:
            self.db = mysql.connector.connect(user=self.username, password=self.password,
                                              host=self.host)
        return self

    def get_db(self):
        return self.db

    def get_cursor(self, **kwargs):
        return self.db.cursor(**kwargs)

    def commit(self):
        self.db.commit()

    def close_db_connection(self):
        self.db.close()
