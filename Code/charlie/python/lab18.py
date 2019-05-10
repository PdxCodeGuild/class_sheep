#Peaks and Valleys
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,   7, 8,   9,  8,  7,  6,  7,  8  ,9] # - y axis


def peak(input_list):
    peak_list_indicies = []
    for index in range(1, len(data) - 1):
        if data[index] > data[index - 1] and data[index] > data[index + 1]:
            peak_list_indicies.append(index)
    return peak_list_indicies
# print(peak(data))

def valley(input_list):
    valley_list_indicies = []
    for index in range(1, len(data) - 1):
        if data[index] < data[index - 1] and data[index] < data[index + 1]:
            valley_list_indicies.append(index)
    return valley_list_indicies
# print(valley(data))
#returns the low points of the


def peaks_and_valleys(input_list):
        peaks_and_valleys_list = []
        for index in range(1, len(data) - 1):
            if data[index] > data[index - 1] and data[index] > data[index + 1]:
                peaks_and_valleys_list.append(index)

            elif data[index] < data[index - 1] and data[index] < data[index + 1]:
                peaks_and_valleys_list.append(index)


            else:
                continue

        return peaks_and_valleys_list


#index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20] - X axis
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,   7, 8,   9,  8,  7,  6,  7,  8  ,9] # - y axis


#run the code from left to write. determine if the x is 'tall enough' to print'''

#V2

low_peak_lake = peak(data)[0]+ 1
high_peak_lake = peak(data)[1]
print(low_peak_lake)
print(high_peak_lake)


maximum = 0
for index in data:
    if index >= data[index + 1] and index >= data[index -1]:
        maximum = index
max_val = maximum
print(maximum)



for index in range(maximum,0 , -1):
    maximum -=1
    while num <= 9:
        for index in range(len(data)):
            if index > maximum:
                print('X', end = ' ')
            elif num[index] != maximum:
                print('O', end = ' ')
            # elif index >= (low_peak_lake) and index <= (high_peak_lake -  1):
            #     print('0', end = ' ')
            else:
                print(' ', end = ' ')


        print()



print(peaks_and_valleys(data))
      # a number between the range 9 and 0.  each iteration steps down 1 ( 9 - 8 -7 - ... - 0)
        #(after each for loop, the max is decreased by 1
        # print(index, end = ' ')



        # if data[index] > peak(data)[index]:
        #     print('O', end = ' ')


#
# first_peak_lake = low_peak_lake
# for num in range(max_val, 0, -1):
#     if max_val[data] < max_val[data] + 1:
#
#     for num in data:
#         print(num, end = ' ')
# print()




# coord_list = []
# for y_coord in range(max_val):
#     temp_list = []
#     for x_coord in range(len(data)):
#         temp_list.append(data[x_coord])
#     coord_list.append(temp_list)
# print(max_val)
# print(coord_list)
