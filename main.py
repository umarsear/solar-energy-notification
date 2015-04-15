__author__ = 'Umar Sear'
import sys
from db_sqlite3 import get_db_row_count, get_site_details, write_energy_to_database, write_power_to_database, touch_site
from solar_edge import get_energy_values, get_power_values
from datetime import date, datetime, timedelta
from sun_stage import its_between_dawn_sunset, its_after_sunset
from email_notification import send_email
from configparser import ConfigParser


parser = ConfigParser()

if len(sys.argv) > 1:
    parser.read(sys.argv[1])
else:
    parser.read('solar_notification.ini')

#  add relative path instead of explicit path
database_name = parser.get('database','dbfilename')


def main():
    row_count = get_db_row_count(database_name, "sites");

    for x in range(1,row_count+1):
        date_time = datetime.now()
        site_details = get_site_details(database_name, x)

        try:
            last_update = date_time.strptime(site_details[7], "%Y-%m-%d").date()

        except:

            last_update = date.today() - timedelta(1)

        if its_between_dawn_sunset(site_details[3]):
            kwhr = get_energy_values(site_details[4], site_details[0], date_time.date())
            write_energy_to_database(database_name, site_details[0], date_time, kwhr)
            print("{}'s solar system produced {} KWhr of electricity so far".format(site_details[2], kwhr))

        elif its_after_sunset(site_details[3]) and (last_update < date_time.date()):
            kwhr = get_energy_values(site_details[4], site_details[0], date_time.date())
            power_values = get_power_values(site_details[4], site_details[0], date_time.date(), date_time.date())
            write_power_to_database(database_name, site_details[0], power_values)
            touch_site(database_name,site_details[0],date_time.date())
            if len(site_details[5]) > 0:
                send_email(site_details[2], site_details[5], 'Solar production notification', kwhr)
            print("{}'s solar system produced {} KWhr of electricity today".format(site_details[2], kwhr))

if __name__ == '__main__':
    sys.exit(main())