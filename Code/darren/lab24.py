#lab24
'''Rain Data'''

import string
import datetime
import requests
import re
import math

'''{Functions}'''

'''Recognizes and removes the datetime from a string'''
def pack_dt(in_string):
    out_string = datetime.datetime.strptime(in_string, '%d-%b-%Y')
    return out_string.strftime('%d-%b-%Y')

'''Version that converts the datetime into split values'''
def unpack_dt(in_string):
    converted = datetime.datetime.strptime(in_string, '%d-%b-%Y')
    day = converted.day
    month = converted.month
    year = converted.year
    out_tuple = (day, month, year)
    return out_tuple

'''Finds the mean of a list of integers'''
def mean_finder(in_list):
    total = 0
    for index in in_list:
        total += index
    length = len(in_list)
    mean = total/length
    return mean

'''Finds the variance of a list of integers'''
def variance_finder(in_list):
    in_list_mean = mean_finder(in_list)
    for i in range(len(in_list)):
        in_list[i] -= in_list_mean
        in_list[i] *= in_list[i]
    variance = mean_finder(in_list)
    variance = math.sqrt(variance)
    return variance

'''Converts tick number to inch value'''
def inch_converter(in_num):
    inches = float(in_num) * 0.01
    return inches

'''Creates a list of dictionaries with the date and rainfall for that day'''
#Example input url: https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain
def load_data():
    url_input = input("Please enter the url on or.water.usgs.gov to analyze: ")
    rain_data = requests.get(url_input)
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
    return rainfall_data_list

'''Retrieves years present in the rainfall_data_list'''
def get_years(rainfall_data_list):
    rainy_years = []
    for index in range(len(rainfall_data_list)):
        split_date = unpack_dt(rainfall_data_list[index]['date'])
        split_year = split_date[2]
        if split_year not in rainy_years:
            rainy_years.append(split_year)
    return rainy_years

'''{Rain Calculator}'''
'''Creates list of tuples with year and mean rainfall'''
rainfall_data_list = load_data()
rainy_years = get_years(rainfall_data_list)
year_tuple_list = []
total_rain_list = []
for item in rainy_years:
    year_rain_list = []
    for index in range(len(rainfall_data_list)):
        total_rain_list.append(rainfall_data_list[index]['rainfall'])
        split_date = unpack_dt(rainfall_data_list[index]['date'])
        split_year = split_date[2]
        if split_year == item:
            year_rain_list.append(rainfall_data_list[index]['rainfall'])
    year_mean = mean_finder(year_rain_list)
    year_mean = inch_converter(year_mean)
    year_tuple = (item, year_mean)
    year_tuple_list.append(year_tuple)

'''Gets the mean and variance for the rainfall of all days'''
total_mean = mean_finder(total_rain_list)
total_variance = variance_finder(total_rain_list)
total_mean = inch_converter(total_mean)
total_variance = inch_converter(total_variance)
print(f"The mean rainfall was {total_mean} of an inch, and the variance was {total_variance} of an inch.")

'''Compares the rainfall averages of each tuple to find the highest'''
def highest_rainfall_average():
    highest_tuple = ''
    highest_mean = 0
    for index in range(len(year_tuple_list)):
        if year_tuple_list[index][1] > highest_mean:
            highest_mean = year_tuple_list[index][1]
    for index in range(len(year_tuple_list)):
        if year_tuple_list[index][1] == highest_mean:
            highest_tuple = year_tuple_list[index]
    print(f"The year with the highest rainfall on average per day was {highest_tuple[0]} with {highest_tuple[1]} of an inch.")
highest_rainfall_average()

'''Calculates the highest rainfall of all days in the chart'''
def highest_rainfall_total():
    highest_date = ''
    highest_rain = 0
    for index in range(len(rainfall_data_list)):
        if rainfall_data_list[index]['rainfall'] > highest_rain:
            highest_date = rainfall_data_list[index]['date']
            highest_rain = rainfall_data_list[index]['rainfall']
    highest_rain = round(inch_converter(highest_rain))
    highest_day = unpack_dt(highest_date)
    print(f"{highest_day[1]}/{highest_day[0]}/{highest_day[2]} had the most rain with roughly {highest_rain} inches.")
highest_rainfall_total()

'''{Graph Version}'''

# '''Generates graph of years and their average rainfall'''
# def year_average_graph():
    # import matplotlib.pyplot as plt
#     x = []
#     y = []
#     for item in range(len(rainy_years)):
#         x.append(rainy_years[item])
#         y.append(year_tuple_list[item][1])
#
#     plt.plot(x, y)
#     plt.xticks(list(range(min(x),max(x)+1)),[str(i) for i in range(min(x),max(x)+1)])
#     plt.xlabel('Year')
#     plt.ylabel('Average Rainfall')
#     plt.show()
# year_average_graph()

'''Generates graph of average rainfall per month of all years.'''
def month_average_graph():
    import matplotlib.pyplot as plt
    rainy_months = []
    for index in range(len(rainfall_data_list)):
        split_date = unpack_dt(rainfall_data_list[index]['date'])
        split_month = split_date[1]
        if split_month not in rainy_months:
            rainy_months.append(split_month)
    rainy_months.sort()
    month_rain_days = []
    month_rain_total = []
    for index in range(len(rainy_months)):
        month_rain_days.append([])
        month_rain_total.append(0)
    for i in range(len(rainfall_data_list)):
        split_date = unpack_dt(rainfall_data_list[i]['date'])
        split_month = split_date[1]
        split_rain = rainfall_data_list[i]['rainfall']
        for j in range(len(rainy_months)):
            if rainy_months[j] == split_month:
                month_rain_days[j].append(split_rain)
    for i in range(len(month_rain_days)):
        for j in range(len(month_rain_days[i])):
            month_rain_total[i] += month_rain_days[i][j]
    for k in range(len(month_rain_total)):
        month_rain_total[k] = month_rain_total[k]/len(month_rain_days[k])
        month_rain_total[k] = round(month_rain_total[k])
        month_rain_total[k] = inch_converter(month_rain_total[k])
    x = rainy_months
    y = month_rain_total
    plt.plot(x, y)
    plt.xlabel('Months')
    plt.ylabel('Average Rainfall (Inches)')
    plt.show()
month_average_graph()

'''{Notes}'''

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
