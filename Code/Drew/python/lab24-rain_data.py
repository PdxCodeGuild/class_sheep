import requests
import re
import datetime
import matplotlib.pyplot as plt

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

# Print top 10 days
print("Sylvania PCC Rain Gage")
print("Dates with Highest Rainfall")
for record in range(10):
    print(f'Date: {rain_sorted[record][0].strftime(date_format)}, Total Rainfall: {rain_sorted[record][1]}')

# Get average by month
jan_list = []
feb_list = []
mar_list = []
apr_list = []
may_list = []
jun_list = []
jul_list = []
aug_list = []
sep_list = []
oct_list = []
nov_list = []
dec_list = []
for i in range(1, 13):
    for tup in rain_record:
        if tup.month == 1:
            jan_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 2:
            feb_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 3:
            mar_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 4:
            apr_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 5:
            may_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 6:
            jun_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 7:
            jul_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 8:
            aug_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 9:
            sep_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 10:
            oct_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 11:
            nov_list.append(rain_record[tup])
    for tup in rain_record:
        if tup.month == 12:
            dec_list.append(rain_record[tup])

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_values = []

jan_rains = sum(jan_list)
jan_avg = jan_rains/len(jan_list)
y_values.append(jan_avg)

feb_rains = sum(feb_list)
feb_avg = feb_rains/len(feb_list)
y_values.append(feb_avg)

mar_rains = sum(mar_list)
mar_avg = mar_rains/len(mar_list)
y_values.append(mar_avg)

apr_rains = sum(apr_list)
apr_avg = apr_rains/len(apr_list)
y_values.append(apr_avg)

may_rains = sum(may_list)
may_avg = may_rains/len(may_list)
y_values.append(may_avg)

jun_rains = sum(jun_list)
jun_avg = jun_rains/len(jun_list)
y_values.append(jun_avg)

jul_rains = sum(jul_list)
jul_avg = jul_rains/len(jul_list)
y_values.append(jul_avg)

aug_rains = sum(aug_list)
aug_avg = aug_rains/len(aug_list)
y_values.append(aug_avg)

sep_rains = sum(sep_list)
sep_avg = sep_rains/len(sep_list)
y_values.append(sep_avg)

oct_rains = sum(oct_list)
oct_avg = oct_rains/len(oct_list)
y_values.append(oct_avg)

nov_rains = sum(nov_list)
nov_avg = nov_rains/len(nov_list)
y_values.append(nov_avg)

dec_rains = sum(dec_list)
dec_avg = dec_rains/len(dec_list)
y_values.append(dec_avg)

print()
print("Average Rainfall per Month:")
print(f"Jan - {jan_avg}")
print(f"Feb - {feb_avg}")
print(f"Mar - {mar_avg}")
print(f"Apr - {apr_avg}")
print(f"May - {may_avg}")
print(f"Jun - {jun_avg}")
print(f"Jul - {jul_avg}")
print(f"Aug - {aug_avg}")
print(f"Sep - {sep_avg}")
print(f"Oct - {oct_avg}")
print(f"Nov - {nov_avg}")
print(f"Dec - {dec_avg}")

plt.plot(x_values, y_values)
plt.gcf().autofmt_xdate()
plt.show()
