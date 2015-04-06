__author__ = 'Umar Sear'
import sys
from db_sqlite3 import get_db_row_count, get_site_details, write_energy_to_database
from solar_edge import get_energy_values, get_power_values
from datetime import date, datetime

# move the dbname to config file and add relative path instead of explicit path
dbname = "/Users/umasear/code/solar-energy-notification/data/solar_notification.db"

def main():
    row_count = get_db_row_count("/Users/umasear/code/solar-energy-notification/data/solar_notification.db","sites");

    for x in range(1,2):
        site_details = get_site_details(dbname,x)
        date_time = datetime.now()
        print(date_time.date())
        print(date_time)
        get_power_values(site_details[4], site_details[0], date_time.date(), date_time.date())
#        kwhr = get_energy_values(site_details[4], site_details[0], date_time.date())
#        write_energy_to_database(dbname, site_details[0],date_time,0,kwhr)
#        print("{}'s solar system produced {} KWhr of electricity".format(site_details[2], kwhr))


if __name__ == '__main__':
    sys.exit(main())