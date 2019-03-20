#lab24
#Rain Data

import string
import datetime
import requests
import re

#{Functions}

#Recongnizes and removes the datetime from a string
def pack_dt(in_string):
    out_string = datetime.datetime.strptime(in_string, '%d-%b-%Y')
    return out_string.strftime('%d-%b-%Y')

#Version that converts the datetime into split values
def unpack_dt(in_string):
    converted = datetime.datetime.strptime(in_string, '%d-%b-%Y')
    day = converted.day
    month = converted.month
    year = converted.year
    out_tuple = (day, month, year)
    return out_tuple

#Finds the mean of a list of integers
def mean_finder(in_list):
    total = 0
    for index in in_list:
        total += index
    length = len(in_list)
    mean = total/length
    return mean

#Converts tick number to inch value
def inch_converter(in_num):
    inches = float(in_num) * 0.01
    return inches

#{Data List Creation}

#Creates a list of dictionaries with the date and rainfall for that day
rain_data = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
text_orig = rain_data.text
regex_date = '(\d+-\w+-\d+)\s+(\d+)'
dates_rainfall = re.findall(regex_date, text_orig)
rain_dict = {}
for index in range(len(dates_rainfall)):
    rain_dict[dates_rainfall[index][0]] = int(dates_rainfall[index][1])
rainfall_data_list = []
for key in rain_dict:
    dt_key = pack_dt(key)
    rainfall_data_list.append({'date': dt_key, 'rainfall': rain_dict[key]})


#{Highest Average Rainfall Year/Day Version}

#Creates lists of years to check then arranges them in a list of tuples (year, rainfall average)
rainy_years = []
for index in range(len(rainfall_data_list)):
    split_date = unpack_dt(rainfall_data_list[index]['date'])
    split_year = split_date[2]
    if split_year not in rainy_years:
        rainy_years.append(split_year)
year_tuple_list = []
for item in rainy_years:
    year_rain_list = []
    target_year = item
    for index in range(len(rainfall_data_list)):
        split_date = unpack_dt(rainfall_data_list[index]['date'])
        split_year = split_date[2]
        if split_year == item:
            year_rain_list.append(rainfall_data_list[index]['rainfall'])
    year_mean = mean_finder(year_rain_list)
    year_mean = inch_converter(year_mean)
    year_tuple = (target_year, year_mean)
    year_tuple_list.append(year_tuple)
highest_tuple = ''
highest_mean = 0

#Compares the rainfall averages of each tuple to find the highest
for index in range(len(year_tuple_list)):
    if year_tuple_list[index][1] > highest_mean:
        highest_mean = year_tuple_list[index][1]
for index in range(len(year_tuple_list)):
    if year_tuple_list[index][1] == highest_mean:
        highest_tuple = year_tuple_list[index]
print(f"The year with the highest rainfall on average per day was {highest_tuple[0]} with {highest_tuple[1]} an inch.")

#Calculates the highest rainfall of all days in the chart
highest_date = ''
highest_rain = 0
for index in range(len(rainfall_data_list)):
    if rainfall_data_list[index]['rainfall'] > highest_rain:
        highest_date = rainfall_data_list[index]['date']
        highest_rain = rainfall_data_list[index]['rainfall']
highest_rain = round(inch_converter(highest_rain))
highest_day = unpack_dt(highest_date)
print(f"{highest_day[1]}/{highest_day[0]}/{highest_day[2]} had the most rain with roughly {highest_rain} inches.")



#{Rough Draft Work}

# checkdate = input("Please enter the date you want to search: ")
# for index in range(len(rainfall_data_list)):
#     for key in rainfall_data_list[index]:
#         if rainfall_data_list[index][key] == checkdate:
#             split_date = unpack_dt(rainfall_data_list[index][key])
#             split_day = split_date.day
#             split_month = split_date.month
#             split_year = split_date.year
#             print(f"The rainfall for {split_month}/{split_day}/{split_year} was {rainfall_data_list[index]['rainfall']}")

# choose_year = input("Please enter the year to determine average total rainfall: ")
# year_rain_list = []
# year_total = 0
# for index in range(len(rainfall_data_list)):
#     split_date = unpack_dt(rainfall_data_list[index]['date'])
#     split_year = str(split_date.year)
#     if split_year == choose_year:
#         year_total += rainfall_data_list[index]['rainfall']
#         year_rain_list.append(rainfall_data_list[index]['rainfall'])
# year_mean = mean_finder(year_rain_list)
# year_mean = inch_converter(year_mean)
# year_total = inch_converter(year_total)
# print(f"The year {choose_year} had {year_total} inches of rainfall. The mean rainfall was {year_mean}.")

# split_date = datetime.datetime.strptime(checkdate, '%d-%b-%Y')
# print(split_date.year)
# print(split_date.month)
# print(split_date.day)
# print(split_date)
# print(split_date.strftime('%d-%b-%Y'))
