#Peaks and Valleys

PV_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8 ,9]
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8 ,9]

data_length = len(data)
# print(data_length)
data.sort()
# print(data)
data_max = data[data_length-1]
# print(data_max)

def peak(input_list):
    peak_list_indicies = []
    for index in range(1, len(PV_list) - 1):
        if PV_list[index] > PV_list[index - 1] and PV_list[index] > PV_list[index + 1]:
            peak_list_indicies.append(index)
    return peak_list_indicies
print(peak(PV_list))

def valley(input_list):
    valley_list_indicies = []
    for index in range(1, len(PV_list) - 1):
        if PV_list[index] < PV_list[index - 1] and PV_list[index] < PV_list[index + 1]:
            valley_list_indicies.append(index)
    return valley_list_indicies
print(valley(PV_list))


def peaks_and_valleys(input_list):
        peaks_and_valleys_list = []
        for index in range(1, len(PV_list) - 1):
            if PV_list[index] > PV_list[index - 1] and PV_list[index] > PV_list[index + 1]:
                peaks_and_valleys_list.append(index)
            elif PV_list[index] < PV_list[index - 1] and PV_list[index] < PV_list[index + 1]:
                peaks_and_valleys_list.append(index)
            else:
                continue

        return peaks_and_valleys_list
print(peaks_and_valleys(PV_list))
