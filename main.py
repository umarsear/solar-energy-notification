__author__ = 'Umar Sear'
import sys
from db_sqlite3 import get_db_row_count, get_site_details, write_energy_to_database, write_power_to_database, touch_site
from solar_edge import get_energy_values, get_power_values
from datetime import date, datetime, timedelta
from sun_stage import its_between_dawn_sunset, its_after_sunset
from email_notification import send_email

# move the dbname to config file and add relative path instead of explicit path
dbname = "/Users/umasear/code/solar-energy-notification/data/solar_notification.db"

def main():
    row_count = get_db_row_count("/Users/umasear/code/solar-energy-notification/data/solar_notification.db","sites");

    for x in range(1,row_count+1):
        date_time = datetime.now()
        site_details = get_site_details(dbname,x)

        try:
            last_update = date_time.strptime(site_details[7], "%Y-%m-%d").date()

        except:

            last_update = date.today() - timedelta(1)

        if its_between_dawn_sunset(site_details[3]):
            kwhr = get_energy_values(site_details[4], site_details[0], date_time.date())
            write_energy_to_database(dbname, site_details[0], date_time, kwhr)
            print("{}'s solar system produced {} KWhr of electricity".format(site_details[2], kwhr))

        elif its_after_sunset(site_details[3]) and (last_update < date_time.date()):
            kwhr = get_energy_values(site_details[4], site_details[0], date_time.date())
            #power_values = get_power_values(site_details[4], site_details[0], date_time.date(), date_time.date())
            #write_power_to_database(dbname,site_details[0],power_values)
            #touch_site(dbname,site_details[0],date_time.date())
            send_email(site_details[2], 'umarsear@gmail.com', 'Solar production notification', kwhr)

    send_email(site_details[2], 'umarsear@gmail.com', 'Solar production notification', 45.60)

if __name__ == '__main__':
    sys.exit(main())