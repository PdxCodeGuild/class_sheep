# peaks_and_valleys
def peaks(input_data):
    peak_list = []
    for index in range(1, len(input_data) - 1):
        if input_data[index - 1] < input_data[index] > input_data[index + 1]:
            peak_list.append(index)
    return peak_list

def valleys(input_data):
    valley_list = []
    for index in range(1, len(input_data) - 1):
        if input_data[index - 1] > input_data[index] < input_data[index + 1]:
            valley_list.append(index)
    return valley_list

def peaks_and_valleys():
    peaks_and_valleys_list = []
    for index in peaks(input_data):
        peaks_and_valleys_list.append(index)
    for index in valleys(input_data):
        peaks_and_valleys_list.append(index)
    peaks_and_valleys_list = sorted(peaks_and_valleys_list)
    return peaks_and_valleys_list

input_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(f"Peaks: {peaks(input_data)} \nValleys: {valleys(input_data)} \nPeaks and valleys: {peaks_and_valleys()}")

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

list_of_peaks = peaks(input_data)

def lake_finder(input_data, list_of_peaks):
    valley_start_list = []
    for i in list_of_peaks:
        valley_start = input_data[i]
        valley_start_list.append(i)
    viewpoint = valley_start - len(valley_start_list)
    while True:
        viewpoint += 1
        if input_data[viewpoint] != 6:
            break
    return [valley_start_list, viewpoint - 1]

print(lake_finder(input_data, list_of_peaks))
