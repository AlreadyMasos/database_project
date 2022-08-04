import pytest
from database.database import Database
from database.TableTest import TableTest
from framework.utils.cfg_parser import ConfigParser

cfg = ConfigParser().get_config()


@pytest.fixture(scope='session')
def work_with_database(request):
    db = Database(cfg['username'], cfg['password'], cfg['host'], cfg['database_name'])
    db.connect()
    table_test = TableTest(db.get_db(), db.get_cursor())

    def insert_and_check():
        table_test.insert_test('tester', 'test_step', 1, 2, 'default_env', 'chrome',1)
        return table_test.check_if_exist('test_step')
    request.addfinalizer(insert_and_check)
