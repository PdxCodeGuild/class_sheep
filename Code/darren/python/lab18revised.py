# lab18revised.py
'''Peaks and Valleys'''

import random

def peak_finder(in_list):
    peak_list = []
    for index in range(len(in_list)):
        if index == len(in_list)-1:
            if in_list[index] > in_list[index - 1]:
                peak_tuple = (index, in_list[index])
                peak_list.append(peak_tuple)
        else:
            if in_list[index] > in_list[index - 1] and in_list[index] > in_list[index + 1]:
                peak_tuple = (index, in_list[index])
                peak_list.append(peak_tuple)
    return peak_list

# random topography

topography = []
prev_num = 0
for index in range(20):
    if index == 0:
        rand_num = random.randint(0,10)
        prev_num = rand_num
        topography.append(rand_num)
    else:
        rand_num = random.randint(prev_num - 1, prev_num + 1)
        while rand_num < 0 or rand_num > 10 or rand_num == topography[index-1]:
            rand_num = random.randint(prev_num -1, prev_num + 1)
        prev_num = rand_num
        topography.append(rand_num)

#test topography

# topography = [9, 8, 7, 6, 5, 4, 5, 4, 3, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1]

print(topography)
peaks = peak_finder(topography)
print(peaks)

highest_top = 0
for num in topography:
    if num > highest_top:
        highest_top = num
print(highest_top, end='\n')

for y in range(highest_top+1):
    for x in range(0, len(topography)):
        if topography[x] > highest_top - y:
            print('x', end=' ')
        if topography[x] <= highest_top - y:
            print(' ', end=' ')
    print()
