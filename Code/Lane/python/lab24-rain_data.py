# Lab 24 - Rain Data
# Load file and parse data
import requests
import re
from datetime import datetime
import math

def load_data():
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain') # load the webpage
    text = response.text
    regex = '(\d+-\w+-\d+)\s+(\d+)'
    results = re.findall(regex, text)

    data = []
    for i in range(len(results)):
        tuple = results[i]
        date = datetime.strptime(tuple[0], '%d-%b-%Y') #to get data into format 'Year-Month-Day'
        daily_total = int(tuple[1])
        rain_dict = {'date': date, 'daily_total': daily_total} # create a dictionary with two key-value pairs, one for the date and the other for the daily total
        data.append(rain_dict) # add each value pair to the dictionary
    return data
data = load_data()

# version 2 ===================================================================

# calculate the average rainfall
total = 0
for row in data:
    total += row['daily_total'] # loop through the dictionary and add up the daily rain for each entry
print(f'Average daily rainfall in inches: {(total/len(data))*0.01}')

# calculate the variance
def rain_variance(data, total):
    average = total/len(data)
    variance = 0
    for row in data:
        variance = variance + (average - row['daily_total']) ** 2
    return math.sqrt(variance/len(data))
print(f'Variance: {rain_variance(data, total)}')

# find the day which had the most rain
most_rainy = 0
saved_row = 0
for row in data:
    if row['daily_total'] > most_rainy:
        most_rainy = row['daily_total']
        saved_row = row
print('The date with the highest recorded rainfall was')
print(saved_row['date'])
print(f'with {most_rainy *.01} inches of rainfall.')

#find the year with the most rain on average
yearly_averages = {}
for row in data:
    yearly_averages[row['date'].year] = []
for row in data:
    yearly_averages[row['date'].year] += [row['daily_total']]

highest_dict = {'average': 0, 'year': 0}
for var_year in yearly_averages:
    if sum(yearly_averages[var_year])/len(yearly_averages[var_year]) > highest_dict['average']:
        highest_dict['average'] = sum(yearly_averages[var_year])/len(yearly_averages[var_year])
        highest_dict['year'] = var_year
print(f"The year with the most rain was {highest_dict['year']} with an average of {highest_dict['average']} inches of rain.")
