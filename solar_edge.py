__author__ = 'Umar Sear'

from urllib import error
from urllib.request import urlopen
import json

base_url = 'https://monitoringapi.solaredge.com/site'
site_detail_url = '/{0}/details?api_key={1}'
site_data_url = '/{0}/dataPeriod?api_key={1}'
site_energy_url = '/{0}/energy?api_key={1}&timeUnit={2}&endDate={3}&startDate={4}'
site_energy_period_url = '/{0}/timeFrameEnergy?api_key={1}&startDate={2}&endDate={3}'
site_power_url = '/{0}/power?api_key={1}&startTime={2}%2000:00:00&endTime={3}%2023:59:59'
site_overview_url = '/{0}/overview?api_key={1}'


def get_power_values(api_key,site_id, start_date, end_date):
    url = base_url+site_power_url.format(site_id, api_key, start_date, start_date)
    response = urlopen(url)
    str_response = response.readall().decode('utf-8')
    print(str_response)


def get_energy_values(api_key, site_id, energy_date):
    url = base_url+site_energy_url.format(site_id, api_key, 'DAY', energy_date, energy_date)
    try:
        response = urlopen(url)
    except error.URLError:
        return -1
    else:
        str_response = response.readall().decode('utf-8')
        try:
            obj = json.loads(str_response)
        except:
            return -1
        else:
            if len(obj['energy']['values']) > 0 :
                energy_value = int(obj['energy']['values'][0]['value'])/1000
            else:
                energy_value = 0
        return energy_value