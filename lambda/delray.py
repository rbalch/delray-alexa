import logging
import requests
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)
URL = 'https://www.delraybeachfl.gov/government/city-departments/parks-and-recreation/beach'


def get_soup(url):
    """Get the soup from a URL."""
    log.debug("Getting soup from %s", url)
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_delray_beach_info():
    """Get the Delray Beach info."""
    date = ''
    flag_color = ''
    air_temperature = ''
    surf_temperature = ''
    hazards = ''
    high_tide = ''
    surf_conditions = ''
    soup = get_soup(URL)

    for rowi, row in enumerate(soup.table.find_all('tr')):
        if rowi == 1:
            date = row.find_all('td')[1].text.strip()
        elif rowi == 2:
            flag_color = row.find_all('td')[1].text.strip().replace('/', 'and')
        elif rowi == 3:
            air_temperature = row.find_all('td')[1].text.strip()
        elif rowi == 4:
            surf_temperature = row.find_all('td')[1].text.strip()
        elif rowi == 6:
            surf_conditions = row.find_all('td')[1].text.strip()\
                .replace('-', ' to ')\
                .replace('ft', ' foot')
        elif rowi == 7:
            hazards = row.find_all('td')[1].text.strip().replace('/', 'and')
        elif rowi == 9:
            high_tide = row.find_all('td')[1].text.strip()

    message = f'For {date}, the flag color is {flag_color}, the air temperature is {air_temperature}, and surf temperature is {surf_temperature}.'
    if hazards:
        message += f' Hazards include {hazards}.'
    message += f' High tide is at {high_tide}. Surf conditions are {surf_conditions}.'
    return message


if __name__ == '__main__':
    print(get_delray_beach_info())
