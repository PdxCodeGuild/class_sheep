# Lab 24: Rain Data
# The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/
# Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.
#
# To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import re
import requests
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/cleveland.rain')
# Alternative link for other neighborhood: https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain
data = response.text
results = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)
results = dict(results)
dates = list(results.keys())
rainfall = list(results.values())
for i in range(len(rainfall)):
    rainfall[i] = int(rainfall[i])

#Version 2
# Now that you've successfully extracted the data, let's done some statistics.

# Find the year which had the most rain on average.

# Calculate the mean of the data.
sum = 0
for i in range(len(rainfall)):
    sum += rainfall[i]
mean = sum / len(rainfall)
print(mean)

# Calculate the variance: subtract the mean from each data point, square each result, find the sum of the squared values, and divide by the length of the data set - 1
import math
total = 0
for i in range(len(rainfall)):
    total += (rainfall[i] - mean)**2
variance = total / (len(rainfall) - 1)
print(variance)

# Find the day that had the most rain.
most_rainfall = max(rainfall)
dates_most_rain = []
for i in range (len(rainfall)):
    if most_rainfall == rainfall[i]:
        dates_most_rain.append(dates[i])
rainfall_in_inches = most_rainfall / 100
print(f"The maximum rainfall was {rainfall_in_inches} inches on {', '.join(dates_most_rain)}.")

# list_of_dates = []
# for i in dates:
#     list_of_dates.append(i)
# import datetime
# dates = []
# for date in list_of_dates:
#     dates.append(datetime.datetime.strptime(date, '%d-%b-%Y'))
