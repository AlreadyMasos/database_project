import random
from database.TableTest import TableTest
from database.database import Database
from framework.utils.cfg_parser import ConfigParser
import pytest_check as check
from time import sleep
from config.testconf import second_test

cfg = ConfigParser().get_config()


def test_step_2_start(second_test):
    db = Database(cfg['username'], cfg['password'], cfg['host'], cfg['database_name'])
    db.connect()
    table_test = TableTest(db.get_db(), db.get_cursor())
    for i in range(len(table_test.get_with_repeating_nums_in_id())):
        sleep(5)
        check.equal(random.randint(1, 5), 3)
        table_test.insert_test('tester2', test_step_2_start.__name__, 1, 2, 'base',
                               'chrome', 2)
