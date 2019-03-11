#lab18.py
# Peaks and Valleys
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
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# pv = peakvalleyfinder(data)
# print(f"This chart has peaks and valleys at indices {pv}.")

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
highestnum = 0
highestnumlist = []
watertotal = 0
for index in range(len(data)):
    if data[index] >= highestnum:
        highestnum = data[index]
        highestnumlist.append(highestnum)

for boxrow in range(highestnum + 2):
    boxrowdif = 10 - boxrow
    for boxcol in range(len(data)):
        if data[boxcol] > boxrowdif:
            print('x', end=' ')
        if data[boxcol] <= boxrowdif:
            if boxcol > 6 and boxcol < 13 and boxrowdif < 7:
                print('0', end=' ')
                watertotal += 1
            if boxcol > 13 and boxrowdif < 9:
                print('0', end=' ')
                watertotal += 1
            if boxcol <= 6:
                print(' ', end=' ')
            if boxcol > 6 and boxcol <=13 and boxrowdif >= 7:
                print (' ', end=' ')


    print()
print(f"The water total is {watertotal}.")
print(highestnumlist)
