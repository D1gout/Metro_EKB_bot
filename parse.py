import requests as requests
from bs4 import BeautifulSoup


def Parse_Time(station: int):
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

    return times
