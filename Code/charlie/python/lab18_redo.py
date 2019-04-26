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

'''my goal is the same as small peak pool, but to get the big peak pool.  i managed to get the tuple with a series of list manipulations instead of a for loop.  it works, but i am unsure i will be able to make it work with a different data set.'''

def big_peak_tuple(dataset, peaks):

    peak2 = peak(data)[1]
    pool2_list = data[peak2+1:len(data)-1]
    pool_start = peak2+1
    pool_end = pool_start + len(pool2_list)-1
    pool2_list.sort()
    height = min(pool2_list)
    pool2_tuple = tuple((pool_start, pool_end, height))
    return(pool2_tuple)
print(f"the big pool tuple {big_peak_tuple(data, peak(data))}")

'''this for-loop runs an if statement for values below the first peak height.
#each time the for-loop runs, the index marking pool location is increased by one.  as long as the pool location does not equal the same value as the big peak, the locations will be appended to the pool list.  The pool end is just the endpoint of the pool.'''

def small_peak_pool(dataset, peaks):

    pool_start = peak(data)[0]# 6
    pool_location1 = pool_start
    pool1_tuple_list = []
    for num in range(data[pool_start]-1):
        pool_location1 += 1
        if data[pool_location1] != data[pool_start]:
            pool1_tuple_list.append(data[pool_location1])
    pool_end = (len(pool1_tuple_list) + pool_start)
    height = min(pool1_tuple_list)
    pool1_tuple = tuple((pool_start, pool_end, height))
    return(pool1_tuple)
print(f"the small pool tuple {small_peak_pool(data, peak(data))}")

'''I want to create the mountain picture using the data set.  To do this, i have to compare the values in the data list to the value above and below.  if the value i am comparing matches a set of criteria, i can place an X.  if not, i place an empty string. to determine how many times i want to run the code, so that the photo can be complete, i need to determine the maximum peak'''

peak1 = (peaks_and_valleys(data)[0])
peak2 = (peaks_and_valleys(data)[2])
#maximum value
maximum = max(data)

'''i want to draw the X's using the data list.  if the index value is greater then the previous value, the the slope is going up.  if it less then the previous value, the slope is going down.'''
pool_list = []
pool_list.append(small_peak_pool(data, peak(data)))
pool_list.append(big_peak_tuple(data, peak(data)))
print(pool_list)
empty_string = ' '
for max in range(maximum, 0, -1):
    for index in range(len(data)):
        if [pool_start, pool_end, height] in pool_list:
            print('O', end = ' ')

    # empty_string = max
    for index in range(1, len(data)):
        if data[index] > max:
            print('X', end = ' ')

        else:
            print(' ', end = ' ')
    print()
