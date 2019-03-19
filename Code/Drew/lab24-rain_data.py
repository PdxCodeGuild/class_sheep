import requests
import re
import datetime

# Get data
r = requests.get('https://or.water.usgs.gov/non-usgs/bes/pcc_sylvania.rain')
rain_data = r.text

# Extract valid matches
regex = '(\d+-\w+-\d{4})\s+(\d+)'
date_rains = re.findall(regex, rain_data)

# Convert dates and sort by value
date_format ='%d-%b-%Y'
rain_record = {}
for tup in date_rains:
    d = datetime.datetime.strptime(tup[0], date_format)
    rain_record[d] = int(tup[1])
rain_sorted = sorted(rain_record.items(), key=lambda tup: tup[1], reverse=True)

# Print top 20 days
print("Sylvania PCC Rain Gage")
print("Dates with Highest Rainfall")
for record in range(20):
    print(f'Date: {rain_sorted[record][0].strftime(date_format)}, Total Rainfall: {rain_sorted[record][1]}')
