#OptionalLab1.py
#Roadtrip
# goto = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
#  }
# usercity = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
# hopbudget = int(input("Enter the number of hops you're willing to take. >"))
# print(f"You can reach {goto[usercity]} from {usercity}.")
# travelguide = list(goto[usercity])
# for city in travelguide:
#     hops = hopbudget
#     hopcities = goto[city]
#     hops -= 1
#     print(hops)
#     print(f"From {city} you can reach {hopcities}.\n")
#     lastvisited = city
#     for city in hopcities:
#         if city == lastvisited:
#             break
#         else:
#             while hops > 1:
#                 hops -= 1
#                 print(hops)
#                 print(f"If you go to {city}...")
#                 print(f"You can reach {goto[city]}.\n")
#                 newhopcities = goto[city]
#                 lastvisited = city
#                 for city in newhopcities:
#                     if city == lastvisited:
#                         break
#                     else:
#                         while hops > 1:
#                             hops -= 1
#                             print(hops)
#                             print(f"If you go to {city}...")
#                             print(f"You can reach {goto[city]}.\n")

goto = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
lastvisited = ''
usercity = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
hops = int(input("How many hops do you want to take? >"))
while hops > 0:
    for city1 in goto.keys():
        entercity = city1
        distlist = []
        for num in goto[entercity].values():
            distlist.append(num)
        distlist.sort()
        print(f"From {city1} you can reach {goto[usercity]}. Shortest distance is {distlist[0]}")
        distlist = []
        for city2 in goto[usercity].keys():
            currentcity = city2
            hops = hops - 1
            print(f"From {currentcity} you can then reach {goto[city2]}.")
    print(f"From {usercity} you can reach {travelguide}.")
    for city in travelguide:
        hops -= 1
        currentcity = city
        citylist = list(goto[currentcity])
        print(f"From {currentcity} you can reach {citylist}.")
