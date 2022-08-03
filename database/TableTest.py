

class TableTest:

    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    def get_all_tests(self):
        query = "SELECT * FROM TEST"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        return all_data

    def get_test_by(self, option, crit):
        query = f"SELECT name FROM TEST WHERE {option} = {crit}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
