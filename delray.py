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

# print(get_soup(URL).prettify())

date = ''
flag_color = ''
air_temperature = ''
surf_temperature = ''
hazards = ''
high_tide = ''
soup = get_soup(URL)

for rowi, row in enumerate(soup.table.find_all('tr')):
    if rowi == 1:
        date = row.find_all('td')[1].text.strip()
    elif rowi == 2:
        flag_color = row.find_all('td')[1].text.strip()
    elif rowi == 3:
        air_temperature = row.find_all('td')[1].text.strip()
    elif rowi == 4:
        surf_temperature = row.find_all('td')[1].text.strip()
    elif rowi == 7:
        hazards = row.find_all('td')[1].text.strip().replace('/', 'and')
    elif rowi == 9:
        high_tide = row.find_all('td')[1].text.strip()

message = f'For {date}, the flag color is {flag_color}, the air temperature is {air_temperature}, the surf temperature is {surf_temperature}, the hazards are {hazards}, and high tide is at {high_tide}.'
print(message)
