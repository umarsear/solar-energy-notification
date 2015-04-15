__author__ = 'umasear'

import os
import unittest
import sys
from db_sqlite3 import get_db_row_count, write_energy_to_database, write_power_to_database, open_database, touch_site
from configparser import ConfigParser


parser = ConfigParser()

if len(sys.argv) > 1:
    parser.read(sys.argv[1])
else:
    parser.read('../solar_notification.ini')


database_name="../data/solar_notification.db"
#database_name = parser.get('database', 'dbfilename')

db = "something.db"


class DatabaseTestCase(unittest.TestCase):

    def test_create_db(self):
        if os.path.isfile(db):
            os.remove(db)
        open_database(db)
        self.assertEqual(True,os.path.isfile(db))

    def test_get_db_row_count(self):
        row_count = get_db_row_count(db, "production")
        self.assertEqual(0, row_count)

    def test_write_energy_to_db(self):
        row_count = get_db_row_count(db, "production")
        write_energy_to_database(db,'1234', '01/01/2015', 100)
        self.assertEqual(row_count+1, get_db_row_count(db, "production"))

    def test_write_Power_to_db(self):
        row_count = get_db_row_count(db, "power")
        write_power_to_database(db, '1234', {"1/1/2015": 1000})
        self.assertEqual(row_count+1, get_db_row_count(db, "power"))

    def test_site_table_db(self):
        row_count = get_db_row_count(db, "sites")
        #write_power_to_database(db, '1234', {"1/1/2015": 1000})
        self.assertEqual(0, get_db_row_count(db, "power"))

    def test_touch_site(self):
        touch_site(db, 123, "1/1/2015")
        self.assertEqual(0, get_db_row_count(db, "power"))

    def test_tidy_up(self):
        if os.path.isfile(db):
            os.remove(db)
        self.assertEqual(False, os.path.isfile(db))

if __name__ == '__main__':
    unittest.main()