import requests
import re
from bs4 import BeautifulSoup

website_url = 'https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/tables/table-8/table-8-state-pieces/table_8_offenses_known_to_law_enforcement_oregon_by_city_2015.xls'
content = requests.get(website_url).text
data = []
soup = BeautifulSoup(content, 'lxml')

table = soup.find('table',{'class':'data'})
table_body = table.find('tbody')
#rows = table_body.find_all('tr')
#print(rows)
#for row in rows:
#    cols = row.find_all('td')
#    cols = [ele.text.strip() for ele in cols]
#    data.append([ele for ele in cols if ele])
#print(data)

city = []
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
for row in table.findAll("tr"):
    cells = row.findAll("td")
    city.append(str(row.find("th").renderContents()))
    if len(cells) == 12:
        populationv = cells[0].find(text=True)
        population.append(re.findall("\d+", populationv))
        violent_crime = cells[1].find(text=True)
        murd_man = cells[2].find(text=True)
        rape = cells[3].find(text=True)
        rape_leg = cells[4].find(text=True)
        robbery = cells[5].find(text=True)
        agg_assault = cells[6].find(text=True)
        property_crime = cells[7].find(text=True)
        burglary = cells[8].find(text=True)
        larc_theft = cells[9].find(text=True)
        veh_theft = cells[10].find(text=True)
        arson = cells[11].find(text=True)
city2 = []
for c in city:
    tempc = re.findall("[A-Z]\w+\s*[A-Z]*\w*",c)
    city2.append(tempc)
print(cells)

#yampop = ''.join(re.findall("\d+",str(cells[0].renderContents())))
#print(yampop)
