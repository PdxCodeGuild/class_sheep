#lab18.py
#Peaks and Valleys
def peakfinder(dict):
    peaklist = []
    for index in range(1, 20):
        if dict[index] > dict[index - 1] and dict[index] > dict[index + 1]:
            peaklist.append(index)
    return peaklist

def valleyfinder(dict):
    valleylist = []
    for index in range(1, 20):
        if dict[index] < dict[index - 1] and dict[index] < dict[index + 1]:
            valleylist.append(index)
    return valleylist

def peakvalleyfinder(dict):
    pvlist = []
    for index in range(1, 20):
        if dict[index] < dict[index - 1] and dict[index] < dict[index + 1]:
            pvlist.append(index)
        if dict[index] > dict[index - 1] and dict[index] > dict[index + 1]:
            pvlist.append(index)
        else:
            continue
    return pvlist


pvdict = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:6, 8:5, 9:4, 10:5, 11:6, 12:7, 13:8, 14:9, 15:8, 16:7, 17:6, 18:7, 19:8, 20:9}
# peaks = peakfinder(pvdict)
# valleys = valleyfinder(pvdict)
pv = peakvalleyfinder(pvdict)
# print(f"This chart has peaks at indices {peaks}.")
# print(f"This chart has valleys at indices {valleys}.")
print(f"This chart has peaks and valleys at indices {pv}.")
