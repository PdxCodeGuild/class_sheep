#lab24
#Rain Data

import string
import datetime
import requests
import re

def date_time_converter(in_string):
    converted = datetime.datetime.strptime(in_string, '%d-%b-%Y')
    return converted.strftime('%d-%b-%Y')

rain_data = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
text_orig = rain_data.text

regex_date = '(\d+-\w+-\d+)\s+(\d+)'
dates_rainfall = re.findall(regex_date, text_orig)
rain_dict = {}
for index in range(len(dates_rainfall)):
    rain_dict[dates_rainfall[index][0]] = int(dates_rainfall[index][1])

# rain_dict = {'19-MAR-2019': 10}
rainfall_data_list = []

for key in rain_dict:
    dt_key = date_time_converter(key)
    rainfall_data_list.append({'date': dt_key, 'rainfall': rain_dict[key]})

print(rainfall_data_list)

checkdate = input("Please enter the date you want to search: ")
for index in range(len(rainfall_data_list)):
    for key in rainfall_data_list[index]:
        if rainfall_data_list[index][key] == checkdate:
            print(f"The rainfall for {checkdate} was {rainfall_data_list[index]['rainfall']}")

# date = datetime.datetime.strptime('19-MAR-2019', '%d-%b-%Y')
# print(date.year)
# print(date.month)
# print(date.day)
# print(date)
# print(date.strftime('%d-%b-%Y'))

# [{'date': datetime , 'rainfall': 0}]
