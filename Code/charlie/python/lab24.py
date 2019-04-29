import re
import requests
import datetime
import matplotlib.pyplot as plt
import math

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/swan_island_pump.rain')
text = response.text
#parse data will return a list of strings including date and daily rainfall
def parse_data():
    regex = (r'(\d+-\D+-\d+)\s+(\d+)')
    results = re.findall(regex,text)
    return results
#setting the results of parse_data to date, i make a list of dates in an integer format using datetime
date = parse_data()

#i am defining the keys for the two types of data i have.  i also created an empty list.
#inside the for loop i iterate over the tuple data, create an empty dictionary, set the first key equal to the date, and the second key equal to the rainfall.  the dictionary is appended to the master list and then the loop is repeated.  keeping the empty dictionary outside of the for-loop caused the keys to point at new values even after they have been appended to the list.  this creates many multiples of a single dictionary and not one dictionary for one index.

keys = ['day', 'rainfall']
master_list = []
for i in range(len(date)):
    data_dict = {}
    data_dict[keys[0]] = datetime.datetime.strptime(date[i][0], '%d-%b-%Y')
    data_dict[keys[1]] = int(date[i][1])
    master_list.append(data_dict)

#this is the average rainfall for Swan Island
sum = 0
for i in range(len(master_list)):
    sum += master_list[i]['rainfall']
mean = round(sum/(len(master_list)),1)

#this is the variance for the dataset for rainfall on Swan Island
summation = 0
for i in range(len(master_list)):
    summation += ((master_list[i]['rainfall'] - mean)**2)
variance = round(summation/(len(master_list)),1)

#this determines the day with the most rain.  i iterate through the list and determine if the current rainfall is greater then the current max.  if true, it becomes the new maximum.  the day variable is then reassigned to the current index.
max_daily_rain = 0
day = ''
for i in range(len(master_list)):
    if (master_list[i]['rainfall']) > max_daily_rain:
        max_daily_rain = (master_list[i]['rainfall'])
        day = (master_list[i]['day'])

#I want to determine the total rainfall per year.  To do this, I created two empty lists, one for year and one for rain.  i set rain = to 0.  i iterate over the master_list.  In the next step, i have an if statement  and i compare the years to each other.  as long as the current indexs year is equal to the next indexs year, the rain is summed up.  once the index points to a differet year, rain is appended to the rain list, the year is appended to the year list and the counter is set to zero.  the loop will continue for each year.
years = []
rain_list = []
rain = 0
for i in range(len(master_list)):
    rain += master_list[i]['rainfall']
    if i == len(master_list)-1 or master_list[i]['day'].year != master_list[i+1]['day'].year:
        years.append(master_list[i]['day'].year)
        rain_list.append(rain)
        rain = 0
#===================ALTERNATIVE=================================
# years = []
# for i in range(len(master_list)):
#     year = master_list[i]['day'].year
#     if year not in years:
#         years.append(year)
# years.sort()
#
# totals = []
# for i in range(len(years)):
#     totals.append(0)
#
# for i in range(len(years)):
#     for j in range(len(master_list)):
#         if years[i] == master_list[i]['day'].year:
#             totals[i] += master_list[i]['rainfall']


#============================ANNUAL RAINFALL==================================
##I want to find the max rainfall.  To do this, i set two max rain to zero. i iterate over the rain_list and for each indicie i compare it to the max rain.  if it's larger, i set the larger rainfall to the max_annual_rain.  I use the same indicie in the years to determine what year had the max rainfall.  i point max_year at that.

# max_year = 0
# max_annual_rain = 0
# for i in range(len(rain_list)):
#     if rain_list[i] > max_annual_rain:
#         max_annual_rain = rain_list[i]
#         max_year = years[i]
#
# for i in range(len(rain_list)):
#     rain_list[i] /= 100
#
# print(years)
# print(rain_list)
# print(f"The year with the most water, {max_annual_rain} was {max_year}")
#
# plt.plot(years, rain_list, 'rs')
# plt.title('Annual precipitaion for Swan Island, OR (2007 to 2019)')
# plt.xlabel('Years')
# plt.ylabel('Annual Rainfall (inches)')
# plt.show()

#======================MONTHLY RAINFALL=======================================
##Generate a graph displaying monthly rain data over the duration of the data

#Take the master data and convert the date into month, year tuple.  i append each individual tuple to the list
month_years_tuple_list = []
for i in range(len(master_list)):
    tuple = (master_list[i]['day'].month, master_list[i]['day'].year)
    if tuple not in month_years_tuple_list:
        month_years_tuple_list.append(tuple)

#try to determine the total rainfall per month.  we create a list that contains the same number of iterations as the tuple list.
totals = []
for i in range(len(month_years_tuple_list)):
    totals.append(0)

#for each iteration, we iterate through the master_list.  if the month value is equal to the month value in both lists, we add the rainfall data at the jth index to the totals list at the ith index.
for i in range(1, len(month_years_tuple_list)):
    for j in range(len(master_list)):
        if month_years_tuple_list[i][0] == master_list[j]['day'].month:
            if month_years_tuple_list[i][1] == master_list[j]['day'].year:
                totals[i] += master_list[j]['rainfall']



months = []
years = []
for i in range(len(month_years_tuple_list)):
    month, year = month_years_tuple_list[i]
    months.append(month)
    years.append(year)

months = []
years = []
month_years_string_list = []
for i in range(len(month_years_tuple_list)):
    month_years_tuple_list[i] = str(month_years_tuple_list[i])
    month_years_string_list.append(month_years_tuple_list[i])

for i in range(len(month_years_string_list)):
    month_years_string_list[i].strip('()')

for i in range(len(totals)):
    totals[i] /= 100
# plt.plot(months, totals, 'ro')
plt.title('Monthly precipitaion for Swan Island, OR (2007 to 2019)')
plt.plot(month_years_string_list, totals)
plt.xlabel('Months')
plt.ylabel('Annual Rainfall (inches)')
plt.show()

print(totals)
# print(month_years_string_list)
