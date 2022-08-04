from framework.utils.random_utils import create_random_string


class AuthorTable:

    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    def insert_author(self):
        name = create_random_string(10)
        email = f'{name}@{create_random_string(4)}.com'
        query = "INSERT INTO AUTHOR (name, login, email) VALUES (%s, %s, %s)"
        data = (name, create_random_string(10), email)
        self.cursor.execute(query, data)
        self.db.commit()
