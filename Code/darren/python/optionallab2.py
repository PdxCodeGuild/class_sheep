# optionallab2.py
'''Sock Sorter'''

import random

# sock_list = []
# sock_types = ['ankle', 'crew', 'calf', 'thigh']
# sock_dict = {'ankle':0, 'crew':0, 'calf':0, 'thigh':0}
#
# for sock in range(100):
#      sock_list.append(sock_types[random.randint(0,3)])
# print(sock_list)
# for i in range(len(sock_list)):
#     sock_dict[sock_list[i]] += 1
#     print(f'{sock_list[i]}, {sock_dict[sock_list[i]]}')
#     print(sock_dict)
# for key in sock_dict.keys():
#     if sock_dict[key] == 1:
#         print(f'{key}, loner.')
#     if sock_dict[key] > 1:
#         pair_total = sock_dict[key] // 2
#         loner_total = sock_dict[key] % 2
#         print(f'{key}, {pair_total} pairs, {loner_total} left over.')
#
sock_list = []
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
sock_dict = {}

for sock in range(100):
    sock_t = sock_types[random.randint(0,3)]
    sock_c = sock_colors[random.randint(0,2)]
    sock_tuple = (sock_t, sock_c)
    sock_list.append(sock_tuple)
print(sock_list)
for sock in sock_list:
    if sock not in sock_dict:
        sock_dict[sock] = 0
for sock in sock_list:
    if sock in sock_dict:
        sock_dict[sock] += 1
    print(f'{sock}, {sock_dict[sock]}')
print(sock_dict)
for key in sock_dict.keys():
    if sock_dict[key] == 1:
        print(f'{key}, loner.')
    if sock_dict[key] > 1:
        pair_total = sock_dict[key] // 2
        loner_total = sock_dict[key] % 2
        print(f'{key}, {pair_total} pairs, {loner_total} left over.')
