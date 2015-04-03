__author__ = 'Umar Sear'

import os
import sqlite3 as lite
from datetime import date,datetime


def open_database(db):
    if os.path.isfile(db):
        db_connection=lite.connect(db)
    else:
        db_connection=lite.connect(db)
        db_cursor=db_connection.cursor()
        db_cursor.execute("CREATE TABLE IF NOT EXISTS production(id integer PRIMARY KEY, siteID integer, "
                          "date TIMESTAMP, time TIMESTAMP, production real, notified integer)")
        db_connection.commit()
    return db_connection, db_connection.cursor()


def write_energy_to_database(db, site_id, energy, notification_sent):
    db_connection, db_cursor=open_database(db)
    db_cursor.execute("INSERT INTO production(siteID, siteName, date, time, production, notified) VALUES(?,?,?,?,?,?)",
                      (site_id, date.today(), datetime.now(), energy, notification_sent))
    db_connection.commit()
    db_connection.close()


def get_site_id(db, db_index):
    db_connection, db_cursor=open_database(db)

def get_site_details(db, site_id):
    db_connection, db_cursor=open_database(db)