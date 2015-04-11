__author__ = 'umasear'

import unittest
import sys
from db_sqlite3 import get_db_row_count
from solar_edge import get_power_values
from configparser import ConfigParser

parser = ConfigParser()

if len(sys.argv) > 1:
    parser.read(sys.argv[1])
else:
    parser.read('../solar_notification.ini')

print(parser.sections())

database_name="../data/solar_notification.db"
#database_name = parser.get('database', 'dbfilename')


class DatabaseTestCase(unittest.TestCase):

    def test_get_db_row_count(self):
        self.assertGreaterEqual(1,0)

    def test_some_random(self):
        self.assertLessEqual(1,9)

if __name__ == '__main__':
    unittest.main()