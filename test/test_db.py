__author__ = 'umasear'

from db_sqlite3 import get_db_row_count, get_site_details
from solar_edge import get_energy_values
from datetime import date

row_count = get_db_row_count("/Users/umasear/code/solar-energy-notification/data/solar_notification.db","sites");

for x in range(1,row_count+1):
    site_details = get_site_details("/Users/umasear/code/solar-energy-notification/data/solar_notification.db",x)
    kwhr = get_energy_values(site_details[4], site_details[0], date.today())
    print("{}'s solar system produced {} KWhr of electricity".format(site_details[2], kwhr))