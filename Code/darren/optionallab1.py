#OptionalLab1.py
#Roadtrip
# city_dict = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
#  }
# user_city = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
# hops = int(input("Enter the number of hops you're willing to take. >"))
# print(f"You can reach {city_dict[user_city]} from {user_city}.")
# travel_guide = list(city_dict[user_city])
# for city in travel_guide:
#     hop_cities = city_dict[city]
#     hops -= 1
#     print(hops)
#     print(f"From {city} you can reach {hop_cities}.\n")
#     last_visited = city
#     for city in hop_cities:
#         if city == last_visited:
#             break
#         else:
#             while hops > 1:
#                 hops -= 1
#                 print(hops)
#                 print(f"If you go to {city}...")
#                 print(f"You can reach {city_dict[city]}.\n")
#                 new_hop_cities = city_dict[city]
#                 last_visited = city
#                 for city in new_hop_cities:
#                     if city == last_visited:
#                         break
#                     else:
#                         while hops > 1:
#                             hops -= 1
#                             print(hops)
#                             print(f"If you go to {city}...")
#                             print(f"You can reach {city_dict[city]}.\n")

import random

def shortest_dist(in_list):
    shortest_num = 10
    for index in range(len(in_list)):
        if in_list[index] < shortest_num:
            shortest_num = in_list[index]
    return shortest_num

city_dict = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
last_visited = ''
user_city = input("Please choose a city: 'Boston', 'New York', 'Albany', 'Portland', 'Philadelphia' >")
hops = int(input("How many hops do you want to take? >"))
already_visited = []
while hops > 0:
    already_visited.append(user_city)
    distance_list = []
    for distance in city_dict[user_city].values():
        distance_list.append(distance)
    print(f"From {user_city} you can reach {city_dict[user_city]}.")
    shortest = shortest_dist(distance_list)
    print(f"Shortest distance is {shortest}")
    for city in city_dict[user_city]:
        if city not in already_visited:
            user_city = city
    hops -= 1
