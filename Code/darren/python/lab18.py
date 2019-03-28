#lab18.py
'''Peaks and Valleys'''

#peak/valley finder

def peak_finder(in_data):
    peak_list = []
    for index in range(len(in_data)):
        if index == 0:
            if in_data[index] > in_data[index + 1]:
                peak_tuple =(index, in_data[index])
                peak_list.append(peak_tuple)
        if in_data[index] > in_data[index - 1] and in_data[index] > in_data[index + 1]:
            peak_tuple =(index, in_data[index])
            peak_list.append(peak_tuple)
    return peak_list
#
# def valley_finder(in_data):
#     valley_list = []
#     for index in range(1, 20):
#         if in_data[index] < in_data[index - 1] and in_data[index] < in_data[index + 1]:
#             valley_list.append(index)
#     return valley_list
#
# def peak_valley_finder(in_data):
#     p_v_list = []
#     for index in range(1, 20):
#         if in_data[index] < in_data[index - 1] and in_data[index] < in_data[index + 1]:
#             p_v_list.append(index)
#         if in_data[index] > in_data[index - 1] and in_data[index] > in_data[index + 1]:
#             p_v_list.append(index)
#         else:
#             continue
#     return p_v_list
#
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1, 9, 9]
# data = [1, 2, 3, 4, 5, 4, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
# pv = peak_valley_finder(data)
# print(f"This chart has peaks and valleys at indices {pv}.")

import random
data = []
prev_num = 0
for index in range(21):
    if index == 0:
        rand_num = random.randint(0,10)
        prev_num = rand_num
        data.append(rand_num)
    else:
        rand_num = random.randint(prev_num - 1, prev_num + 1)
        while rand_num < 0 or rand_num > 10 or rand_num == data[index-1]:
            rand_num = random.randint(prev_num -1, prev_num + 1)
        prev_num = rand_num
        data.append(rand_num)
print(data)

peaks1 = peak_finder(data)

print(peaks1)

# # lake finder
# def lake_finder(in_list):
#     peak_list = []
#     result_list = []
#     highest_peak = 0
#     for index in range(len(in_list)):
#         if index == 0:
#             if in_list[index + 1] < in_list[index]:
#                 peak_list.append((index, in_list[index]))
#                 highest_peak = in_list[index]
#         elif index == len(in_list) -1:
#             if in_list[index - 1] < in_list[index]:
#                 peak_list.append((index, in_list[index]))
#                 highest_peak = in_list[index]
#         elif index > 0 and index < len(in_list) - 1:
#             if in_list[index - 1] < in_list[index] and in_list[index + 1] < in_list[index]:
#                 if in_list[index] >= highest_peak:
#                     peak_list.append((index, in_list[index]))
#                     highest_peak = in_list[index]
#         elif in_list[index] == highest_peak and (index, in_list[index]) not in peak_list:
#             peak_list.append((index, in_list[index]))
#     for index in range(len(peak_list) -1):
#         previous_num = 0
#         if index == 0:
#             if peak_list[index][1] != 0:
#                 previous_num = peak_list[index][1]
#                 result_list.append((peak_list[index][0], peak_list[index + 1][0], peak_list[index][1]))
#         elif index == len(peak_list)-2:
#             if peak_list[index][1] != peak_list[index - 1][1]:
#                 previous_num = peak_list[index][1]
#                 result_list.append((peak_list[index][0], peak_list[index + 1][0], peak_list[index][1]))
#         elif peak_list[index][1] != peak_list[index - 1][1]:
#             previous_num = peak_list[index][1]
#             if (peak_list[index][0], peak_list[index + 1][0], peak_list[index][1]) not in result_list:
#                 result_list.append((peak_list[index][0], peak_list[index + 1][0], peak_list[index][1]))
#     print(peak_list)
#     print(result_list)
#     print(highest_peak)
# peaks = lake_finder(data)
# print(peaks)

#water calculator
#random data version

# import random
# data = []
# prev_num = 0
# for index in range(21):
#     if index == 0:
#         rand_num = random.randint(0,10)
#         prev_num = rand_num
#         data.append(rand_num)
#     else:
#         rand_num = random.randint(prev_num - 1, prev_num + 1)
#         while rand_num < 0:
#             rand_num = random.randint(prev_num, prev_num + 1)
#         while rand_num > 10:
#             rand_num = random.randint(prev_num - 1, prev_num)
#         prev_num = rand_num
#         data.append(rand_num)
# print(data)

# water calculator
# preset data version

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1, 9]
# data= [7, 7, 8, 8, 7, 7, 6, 7, 7, 6, 7, 6, 6, 6, 5, 5, 4, 5, 4, 4, 5]
#
# water_total = 0
# for box_row in range(10):
#     last_peak = 1
#     box_row_dif = 10 - box_row
#     for box_col in range(len(data)):
#         if data[box_col] >= last_peak:
#             last_peak = data[box_col]
#         if data[box_col] > box_row_dif:
#             print('x', end=' ')
#         if data[box_col] <= box_row_dif:
#             if data[box_col - 1] > data[box_col] and box_row_dif < last_peak:
#                 print('0', end=' ')
#                 water_total += 1
#             if data[box_col - 1] < data[box_col] and box_row_dif < last_peak:
#                 print('0', end=' ')
#                 water_total += 1
#             if data[box_col - 1] == data[box_col] and box_row_dif < last_peak:
#                 print('0', end=' ')
#                 water_total += 1
#             if box_col < data[last_peak] and box_row_dif >= last_peak:
#                 print(' ', end=' ')
#             if box_col > data[last_peak] and box_row_dif >= last_peak:
#                 print (' ', end=' ')
#             if box_col == data[last_peak]and box_row_dif >= last_peak:
#                 print(' ', end=' ')
#     print()
# print(f"The water total is {water_total}.")

#rough draft

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# peaks = [7, 9]

# highest_num = 0
# highest_num_list = []
# for index in range(len(data)):
#     if data[index] >= highest_num:
#         highest_num = data[index]
#         highest_num_list.append(highest_num)
# print(highest_num_list)

# def lake_finder(data_list, peak_list):
#     out_list = []
#     for index in range(len(data_list)):
#         if data_list[index] in peak_list:
#             print(index)
#             print(data_list[index])
#             print(out_list)
#             out_list.append((index, data_list[index]))
#     return(out_list)
# lakes = lake_finder(data, peaks)
# print(lakes)
