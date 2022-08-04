import pytest
from database.database import Database
from database.TableTest import TableTest
from framework.utils.cfg_parser import ConfigParser

cfg = ConfigParser().get_config()


@pytest.fixture(scope='session')
def first_test(request):
    db = Database(cfg['username'], cfg['password'], cfg['host'], cfg['database_name'])
    db.connect()
    table_test = TableTest(db.get_db(), db.get_cursor())

    def insert_and_check():
        table_test.insert_test('tester', 'test_step', 1, 2, 'default_env', 'chrome',1)
        return table_test.check_if_exist('test_step')
    request.addfinalizer(insert_and_check)
    db.close_db_connection()


@pytest.fixture(scope='session')
def second_test(request):
    db = Database(cfg['username'], cfg['password'], cfg['host'], cfg['database_name'])
    db.connect()

    def final():
        table_test = TableTest(db.get_db(), db.get_cursor())
        for i in range(len(table_test.get_with_repeating_nums_in_id())):
            table_test.delete_row('tester2')
    request.addfinalizer(final)
    db.close_db_connection()
