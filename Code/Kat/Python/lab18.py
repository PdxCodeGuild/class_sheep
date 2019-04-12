# Lab 18: Peaks and Valleys

#INSTRUCTIONS
# Define the following functions:
# 1. peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# 2. valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# 3. peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

#function for finding peaks
def peaks(input_data):
    peak_list = []
    for index in range(1, len(input_data) - 1):
        if input_data[index - 1] < input_data[index] > input_data[index + 1]:
            peak_list.append(index)
    return peak_list

#function for finding valleys
def valleys(input_data):
    valley_list = []
    for index in range(1, len(input_data) - 1):
        if input_data[index - 1] > input_data[index] < input_data[index + 1]:
            valley_list.append(index)
    return valley_list

#function to combine peaks and valleys into one list
def peaks_and_valleys():
    peaks_and_valleys_list = []
    for index in peaks(input_data):
        peaks_and_valleys_list.append(index)
    for index in valleys(input_data):
        peaks_and_valleys_list.append(index)
    peaks_and_valleys_list = sorted(peaks_and_valleys_list)
    return peaks_and_valleys_list

input_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(f'Peaks: {peaks(input_data)} \nValleys: {valleys(input_data)} \nPeaks and valleys: {peaks_and_valleys()}')

#Version 2
#INSTRUCTIONS: Using the data list above, draw the image of X's above.

def draw(input_data):
    for y in range(9, 0, -1):
        row = ''
        for x in range(0, 21):
            if y <= input_data[x]:
                row += 'X '
            else:
                row += '  '
        print(row)

draw(input_data)


#Version 4 (attempt)
#INSTRUCTIONS: Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

# list_of_peaks = peaks(input_data)
#
# def lake_finder(input_data, list_of_peaks):
#     valley_start_list = []
#     for i in list_of_peaks:
#         valley_start = input_data[i]
#         valley_start_list.append(i)
#     viewpoint = valley_start - len(valley_start_list)
#     while True:
#         viewpoint += 1
#         if input_data[viewpoint] != 6:
#             break
#     return [valley_start_list, viewpoint - 1]
#
# print(lake_finder(input_data, list_of_peaks))
