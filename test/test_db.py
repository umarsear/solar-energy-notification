__author__ = 'umasear'

import unittest
from db_sqlite3 import get_db_row_count
from configparser import ConfigParser

parser = ConfigParser()
parser.read('../solar_notification.ini')
database_name = parser.get('database', 'dbfilename')


class DatabaseTestCase(unittest.TestCase):

    def test_get_db_row_count(self):
        self.assertGreaterEqual(get_db_row_count(database_name, "sites"),0)

if __name__ == '__main__':
    unittest.main()