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

maximum = 0
for value in data:
    if value >= data[value + 1] and value >= data[value -1]:
        maximum = value


for num in range(maximum,0 , -1):
    maximum -=1
    for num in data:
        if num > maximum:
            print('X', end = ' ')
        else:
            print(' ', end = ' ')
    print()
