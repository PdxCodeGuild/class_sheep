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
while hops > 0:
    for city1 in city_dict.keys():
        enter_city = city1
        dist_list = []
        for num in city_dict[enter_city].values():
            dist_list.append(num)
        dist_list.sort()
        print(f"From {city1} you can reach {city_dict[user_city]}. Shortest distance is {dist_list[0]}")
        dist_list = []
        for city2 in city_dict[user_city].keys():
            current_city = city2
            hops = hops - 1
            print(f"From {current_city} you can then reach {city_dict[city2]}.")
    print(f"From {user_city} you can reach {travel_guide}.")
    for city in travel_guide:
        hops -= 1
        current_city = city
        city_list = list(city_dict[current_city])
        print(f"From {current_city} you can reach {city_list}.")
