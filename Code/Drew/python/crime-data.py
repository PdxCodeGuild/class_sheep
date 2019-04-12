import requests
import re
from bs4 import BeautifulSoup

# Get crime data from FBI website
website_url = 'https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/tables/table-8/table-8-state-pieces/table_8_offenses_known_to_law_enforcement_oregon_by_city_2015.xls'
content = requests.get(website_url).text
soup = BeautifulSoup(content, 'lxml')
table = soup.find('table',{'class':'data'})

# Initialize lists
f_city = []
population = []
violent_crime = []
murd_man = []
rape = []
rape_leg = []
robbery = []
agg_assault = []
property_crime = []
burglary = []
larc_theft = []
veh_theft = []
arson = []

# Get the crime data from the HTML table
for row in table.findAll("tr"):
    cells = row.findAll("td")
    f_city.append(str(row.find("th").renderContents()))
    if len(cells) == 12:
        population.append(''.join(re.findall("\d+",str(cells[0].renderContents()))))
        violent_crime.append(''.join(re.findall("\d+",str(cells[1].renderContents()))))
        murd_man.append(''.join(re.findall("\d+",str(cells[2].renderContents()))))
        rape.append(''.join(re.findall("\d+",str(cells[3].renderContents()))))
        rape_leg.append(''.join(re.findall("\d+",str(cells[4].renderContents()))))
        robbery.append(''.join(re.findall("\d+",str(cells[5].renderContents()))))
        agg_assault.append(''.join(re.findall("\d+",str(cells[6].renderContents()))))
        property_crime.append(''.join(re.findall("\d+",str(cells[7].renderContents()))))
        burglary.append(''.join(re.findall("\d+",str(cells[8].renderContents()))))
        larc_theft.append(''.join(re.findall("\d+",str(cells[9].renderContents()))))
        veh_theft.append(''.join(re.findall("\d+",str(cells[10].renderContents()))))
        arson.append(''.join(re.findall("\d+",str(cells[11].renderContents()))))

# Use regex to better extract city names
city = []
f_city.pop(0)
for c in f_city:
    tempc = re.findall(r"[A-Z]\w+\s*-?[A-Z]*\w*",c)
    city.append(tempc)

# If value is '', change to 0 (rape definition changed)
#for i in range(len(rape)):
#    if rape[i] == '':
#        rape[i] = 0
#for i in range(len(rape_leg)):
#    if rape_leg[i] == '':
#        rape_leg[i] = 0

# Combining rape definitions (sloppy, but just for practice)
for i in range(len(rape)):
    if rape[i] == '':
        rape[i] = rape_leg[i]

# Sunriver is the only blank population
for i in range(len(population)):
    if population[i] == '':
        population[i] = 1400

# Organize the data in a dictionary
crime_dict = {}
for i in range(len(city)):
    crime_dict.update({city[i][0]:[int(population[i]), int(violent_crime[i]), int(murd_man[i]), int(rape[i]), int(robbery[i]), int(agg_assault[i]), int(property_crime[i]), int(burglary[i]), int(larc_theft[i]), int(veh_theft[i]), int(arson[i])]})

# Allow user to lookup data by crime
while True:
    try:
        user_choice = int(input("For which crime would you like to see stats?:\n1 - Violent Crime\n2 - Murder/Manslaughter\n3 - Rape\n4 - Robbery\n5 - Aggrivated Assault\n6 - Property Crime\n7 - Burglary\n8 - Larceny/Theft\n9 - Vehicle Theft\n10 - Arson\n"))
        for city in crime_dict:
            print(f"{city} (pop. {crime_dict[city][0]}) - {crime_dict[city][user_choice]}")
        break
    except ValueError:
        print("Try Again")
