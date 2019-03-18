# lab18revised.py
# Peaks and Valleys
import random

def peak_finder(in_list):
    peak_list = []
    for index in range(len(in_list)):
        if index == 0:
            if in_list[index] > in_list[index + 1]:
                peak_tuple = (index, in_list[index])
                peak_list.append(peak_tuple)
        elif index == len(in_list)-1:
            if in_list[index] > in_list[index - 1]:
                peak_tuple = (index, in_list[index])
                peak_list.append(peak_tuple)
        else:
            if in_list[index] > in_list[index - 1] and in_list[index] > in_list[index + 1]:
                peak_tuple = (index, in_list[index])
                peak_list.append(peak_tuple)
    return peak_list

def lake_finder(peak_list, topography):
    lake_list = []
    for peak in range(len(peak_list)):
        if peak_list[peak][1] > peak_list[peak + 1][1]:
            height = peak_list[peak + 1][1]
            east = peak_list[peak + 1][0]
            for index in range(len(topography):
                if topography[index] == height:
                    search_point = index
            for index in range(len(topography[0][search_point])):
                if topography[index] == peak_list[peak + 1][1]:
                    west = index
            lake_tuple = (west, east, height)
            lake_list.append(lake_tuple)
        if peak_list[peak][1] < peak_list[peak + 1][1]:
            height = peak_list[peak][1]
            west = peak_list[peak][0]
            for index in range(len(topography):
                if topography[index] == height and topography[index] < topography[index + 1]:
                    search_point = index
            for index in range(len(topography[0][search_point])):



topography = []
prev_num = 0
for index in range(21):
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

print(topography)

peaks1 = peak_finder(topography)

print(peaks1)
