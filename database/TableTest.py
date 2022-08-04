

class TableTest:

    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    def get_all_tests(self):
        query = "SELECT * FROM TEST;"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        return all_data

    def get_test_by(self, option, crit):
        query = "SELECT name FROM TEST WHERE %s = %s"
        data = (option, crit)
        self.cursor.execute(query, data)
        result = self.cursor.fetchall()
        return result

    def insert_test(self, name, method_name, project_id, session_id, env, browser, author_id):
        query = "INSERT INTO TEST (name, method_name, project_id, session_id, env, browser, author_id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"
        data = (name, method_name, project_id, session_id, env, browser, author_id)
        self.cursor.execute(query, data)
        self.db.commit()

    def check_if_exist(self, name):
        data = self.get_test_by('method_name', name)
        return len(data) >= 1

    def get_with_repeating_nums_in_id(self, number):
        query = "SELECT author, project_id FROM TEST WHERE ID = %s"
        data = (number)
        self.cursor.execute(query, data)
        show = self.cursor.fetchall()