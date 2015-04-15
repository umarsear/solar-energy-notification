__author__ = 'Umar Sear'

import os
import sqlite3 as lite

def open_database(db):
    """
    :rtype : sqlite3 database connection
    """
    if os.path.isfile(db):
        db_connection = lite.connect(db)
    else:
        db_connection = lite.connect(db)
        db_cursor = db_connection.cursor()

        db_cursor.execute("CREATE TABLE IF NOT EXISTS production(id INTEGER PRIMARY KEY, site_id INTEGER, "
                          "date TIMESTAMP, datetime TIMESTAMP, energy REAL, notified INTEGER)")

        db_cursor.execute("CREATE TABLE IF NOT EXISTS power (id	INTEGER NOT NULL, site_id INTEGER NOT NULL,"
                          "time_stamp TIMESTAMP, power_level REAL, PRIMARY KEY(id))")

        db_cursor.execute('CREATE TABLE IF NOT EXISTS sites (id	INTEGER NOT NULL, site_id INTEGER NOT NULL, '
                          'site_name TEXT NOT NULL, site_owner TEXT NOT NULL, closest_capital_city TEXT NOT NULL, '
                          'api_key TEXT NOT NULL, email_address TEXT NOT NULL, pushover_user_key INTEGER, '
                          'last_update	TIMESTAMP, PRIMARY KEY(id)) ')

        db_connection.commit()
    return db_connection


def write_energy_to_database(db, site_id, date_time, energy):
    db_connection = open_database(db)
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO production(site_id, datetime,  energy) VALUES(?,?,?)",
                      (site_id, date_time, energy))
    db_connection.commit()
    db_connection.close()


def write_power_to_database(db, site_id, power_values):
    db_connection = open_database(db)
    db_cursor = db_connection.cursor()

    for date_time, power in power_values.items():
        db_cursor.execute("INSERT INTO power(site_id, time_stamp,  power_level) VALUES(?,?,?)",
                          (site_id, date_time, power))

    db_connection.commit()
    db_connection.close()


def touch_site(db, site_id, touch_date):
    db_connection = open_database(db)
    db_cursor = db_connection.cursor()
    db_cursor.execute("UPDATE sites SET last_update=? WHERE site_id=?", (touch_date, site_id))
    db_connection.commit()
    db_connection.close()


def get_db_row_count(db, table_name, where_clause=""):
    if where_clause == "":
        query = "SELECT COUNT(*) FROM {}".format(table_name)
    else:
        query = "SELECT COUNT(*) FROM {} WHERE {}".format(table_name, where_clause)

    db_connection = open_database(db)
    db_cursor = db_connection.cursor()
    db_cursor.execute(query)
    count = db_cursor.fetchall()
    return count[0][0]


def get_site_details(db, db_index):
    db_connection = open_database(db)
    db_cursor = db_connection.cursor()
    query = "SELECT site_id, site_name, site_owner, closest_capital_city, api_key, email_address, pushover_user_key," \
            " last_update FROM sites WHERE id={}".format(db_index)
    db_cursor.execute(query)
    row = db_cursor.fetchall()
    return row[0]