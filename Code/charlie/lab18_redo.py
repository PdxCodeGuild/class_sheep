#lab18.py redo

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,  7, 8,  9, 8, 7, 6, 7, 8, 9]


#this determines the indicies where the high values are located
def peak(input_list):
    peak_list_indicies = []
    for index in range(1, len(data) - 1):
        if data[index] > data[index - 1] and data[index] > data[index + 1]:
            peak_list_indicies.append(index)
    return peak_list_indicies


#this determines the indicies where the low values are located
def valley(input_list):
    valley_list_indicies = []
    for index in range(1, len(data) - 1):
        if data[index] < data[index - 1] and data[index] < data[index + 1]:
            valley_list_indicies.append(index)
    return valley_list_indicies

#returns the low points of the

#this combines the information of both peak and valley indicies
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

#i want to use the data list and then determine the span of the lake based on the peak and maybe the

'''this for-loop runs an if statement for values below the first peak height.
#each time the for-loop runs, the index marking pool location is increased by one.  as long as the pool location does not equal the same value as the big peak, the locations will be appended to the pool2 list.  The pool end is just the endpoint of the pool.'''
def big_peak_tuple(dataset, peaks):
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,  7, 8,  9, 8, 7, 6, 7, 8, 9]
    peak2 = peak(data)[1]
    pool2_location = peak2
    pool2_tuple_list = []
    print(pool2_location)
    print(range(data[peak2]))

    for num in range(data[peak2]):
        pool2_location += 1
        if data[peak2] != pool2_location:
            pool2_tuple_list.append(data[peak2])

    pool2_end = (len(pool2_tuple_list) + peak2)
    height2 = min(pool2_tuple_list)
    pool2_tuple = tuple((peak2, pool2_end, height2))
    return(pool2_tuple)

print(big_peak_tuple(data, peak(data)))

'''my goal is the same as big peak pool, but to get the small peak pool'''
def small_peak_pool(dataset, peaks):
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,  7, 8,  9, 8, 7, 6, 7, 8, 9]
    peak1 = peak(data)[0]# 6
    pool_location1 = peak1
    pool1_tuple_list = []
    for num in range(data[peak1]-1):
        pool_location1 += 1
        print(pool_location1)
        if data[pool_location1] != data[peak1]:
            pool1_tuple_list.append(data[pool_location1])
    pool_end = (len(pool1_tuple_list) + peak1)
    height = min(pool1_tuple_list)
    pool1_tuple = tuple((peak1, pool_end, height))
    return(pool1_tuple)

# print(small_peak_pool(data, peak(data)))


'''I want to create the mountain picture using the data set.  To do this, i have to compare the values in the data list to the value above and below.  if the value i am comparing matches a set of criteria, i can place an X.  if not, i place an empty string. to determine how many times i want to run the code, so that the photo can be complete, i need to determine the maximum peak'''
#
# peak1 = (peaks_and_valleys(data)[0])
# peak2 = (peaks_and_valleys(data)[2])
# print(f"peak 1 : {peak1}")
# print(f"peak 2 : {peak2}")
# #maximum value
# maximum = max(data)
# print(maximum)



#i want to draw the X's using the data list.  if the index value is greater then the previous value, the the slope is going up.  if it less then the previous value, the slope is going down.
# empty_string = ' '
#
# for max in range(maximum, 0, -1):
#     # empty_string = max
#     for index in range(1, len(data)):
#         if data[index] > max:
#             print('X', end = ' ')
#
#         else:
#             print(' ', end = ' ')
#
#
#
#     print()
