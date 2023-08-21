import requests as requests
import re
from bs4 import BeautifulSoup


def Parse_Time(station: int, direction: int):
    __IP = 'https://metro-ektb.ru/podrobnyy-grafik-'

    station_list = ['0',
                    '1-1',
                    'st-uralmash',
                    'st-mashinostroiteley',
                    'st-uralskaya',
                    'st-dinamo',
                    'st-ploschad-1905-goda',
                    'st-geologicheskaya',
                    'st-chkalovskaya',
                    'st-botanicheskaya']

    __STATION = station_list[station]

    req = requests.get(__IP + __STATION).text

    soup = BeautifulSoup(req, "lxml")

    times = soup.find('div', class_="uss_catalog_content").find_all('li')

    split_string = times[direction].text.replace(',', '')

    # split_string.re.split(r'\d{3}', '').split(';')

    text = re.sub(r'\s+|$', '', split_string)
    text = re.sub(r':\d{4}', '', text)

    return text


print(Parse_Time(5, 0))
