# Lab 24: Rain Data
# The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/
# Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.
# To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import re
import requests
from datetime import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/cleveland.rain')
# Alternative link for other neighborhood: https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain
data = response.text
results = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)
# years = re.findall(r'20\d{2}|19\d{2}', data)
# print(type(years))
results = dict(results)
dates = list(results.keys())
rainfall = list(results.values())
for i in range(len(rainfall)):
    rainfall[i] = int(rainfall[i])
    dates[i] = datetime.strptime(dates[i], '%d-%b-%Y')


#Version 2
# Now that you've successfully extracted the data, let's done some statistics.
# Find the year which had the most rain on average.
# Calculate the mean of the data.
def rainfall_mean(data):
    sum = 0
    for i in range(len(rainfall)):
        sum += rainfall[i]
        mean = sum / len(rainfall)
    return mean
print(rainfall_mean(data))
# Calculate the variance: subtract the mean from each data point, square each result, find the sum of the squared values, and divide by the length of the data set - 1
import math
def find_variance(data):
    total = 0
    mean = rainfall_mean(data)
    for i in range(len(rainfall)):
        total += (rainfall[i] - mean)**2
        variance = total / (len(rainfall) - 1)
    return variance
print(find_variance(data))
# Find the day that had the most rain.
def max_rainfall(data):
    most_rainfall = max(rainfall)
    return most_rainfall

def day_most_rain(data):
    dates_most_rain = []
    for i in range (len(rainfall)):
        if max_rainfall(data) == rainfall[i]:
            dates_most_rain.append(dates[i].strftime('%d-%b-%Y'))
    return ', '.join(dates_most_rain)

print(f'The maximum rainfall was {max_rainfall(data) / 100} inches on {day_most_rain(results)}.')

#
# years_list = []
# for date in dates:
#     if date.year not in years_list:
#         years_list.append(date.year)
#     years_list.sort()
#
#
# in_list = []
# for year in years_list:
#     for date in dates:
#         if date.year in years_list:
#             in_list.append(date.year)
