
import re
import requests

url = 'https://or.water.usgs.gov/non-usgs/bes/'


def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations


def get_file(location):
    response = requests.get(url + location)
    text = response.text
    results = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', text)
    results = dict(results)
    dates = results.keys()
    rainfall = list(results.values())
    rainfall = [int(rain) for rain in rainfall]
    mean = sum(rainfall) / len(rainfall)

    variance = 0
    for i in range(len(rainfall)):
        variance += (rainfall[i] - mean)**2
    variance /= len(rainfall)-1
    print(variance)




locations = get_locations()

print('which location would you like to see?')
for i in range(len(locations)):
    print(f'\t{i} {locations[i]}')

location_index = int(input('> '))

print(get_file(locations[location_index]))
