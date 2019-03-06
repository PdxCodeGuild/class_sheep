#OptionalLab1.py
#Roadtrip
# citiesaccessible = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
#  }
# usercity = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
# print(f"You can reach {goto[usercity]} from {usercity}.")
# travelguide = list(goto[usercity])
# for city in travelguide:
#     hopcities = goto[city]
#     print(f"From {city} you can reach {hopcities}.")

goto = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
lastvisited = ''
hopbudget = 0
usercity = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
hops = int(input("How many hops do you want to take? >"))
while hops > 0:
    travelguide = list(goto[usercity])
    print(f"From {usercity} you can reach {travelguide}.")
    for city in travelguide:
        hops -= 1
        currentcity = city
        citylist = list(goto[currentcity])
        print(f"From {currentcity} you can reach {citylist}.")
