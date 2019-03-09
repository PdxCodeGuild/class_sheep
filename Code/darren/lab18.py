#lab18.py
#Peaks and Valleys
# def peakfinder(indata):
#     peaklist = []
#     for index in range(1, 20):
#         if indata[index] > indata[index - 1] and indata[index] > indata[index + 1]:
#             peaklist.append(index)
#     return peaklist
#
# def valleyfinder(indata):
#     valleylist = []
#     for index in range(1, 20):
#         if indata[index] < indata[index - 1] and indata[index] < indata[index + 1]:
#             valleylist.append(index)
#     return valleylist
#
# def peakvalleyfinder(indata):
#     pvlist = []
#     for index in range(1, 20):
#         if indata[index] < indata[index - 1] and indata[index] < indata[index + 1]:
#             pvlist.append(index)
#         if indata[index] > indata[index - 1] and indata[index] > indata[index + 1]:
#             pvlist.append(index)
#         else:
#             continue
#     return pvlist
#
#
# # pvdict = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:6, 8:5, 9:4, 10:5, 11:6, 12:7, 13:8, 14:9, 15:8, 16:7, 17:6, 18:7, 19:8, 20:9}
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# # peaks = peakfinder(pvdict)
# # valleys = valleyfinder(pvdict)
# pv = peakvalleyfinder(data)
# # print(f"This chart has peaks at indices {peaks}.")
# # print(f"This chart has valleys at indices {valleys}.")
# print(f"This chart has peaks and valleys at indices {pv}.")

def lakefinder(inlist):
    lakeindexes = []
    for index in range(0, 20):
        if inlist[index] > inlist[index +1]:
            lakeindexes.append((index, inlist[index]))
    return lakeindexes
barf = lakefinder(data)
print(barf)

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# highestnum = 0
# for index in range(len(data)):
#     if data[index] >= highestnum:
#         highestnum = data[index]
#
# for boxrow in range(highestnum + 2):
#     for boxcol in range(len(data)):
#         if data[boxcol] > 10 - boxrow:
#             print('x', end=' ')
#         if data[boxcol] <= 10 - boxrow:
#             print(' ', end=' ')
    #
    # print()
# for ycoord in range(10):
#     for xcoord in range(0, 21):
#         if [xcoord, ycoord] in pvlist:
#             print('*', end=' ')
#         else:
#             print('.', end=' ')
#     print()
