# PV_list = [[1, 0], [2, 1], [3, 2], [4,3], [5,4], [6,5], [7,6], [6,7], [5,8], [4,9], [5,10], [6,11],   [7,12], [8,13],   [9,14],  [8,15],  [7,16],  [6,17] , [7,18],  [8,19], [9,20]]
PV_list = [[1, 0], [2, 1], [3, 2], [4,3], [5,4], [6,5], [7,6], [6,7], [5,8], [4,9], [5,10], [6,11],   [7,12], [8,13],   [9,14],  [8,15],  [7,16],  [6,17] , [7,18],  [8,19], [9,20]]


for x_coord in range(21):
    for y_coord in range(10):
        if [y_coord, x_coord] < PV_list[x_coord]:
            print('X', end=' ')
        else:
            print('', end=' ')
    print()

# for x_coord in range(0, 21):
#     for y_coord in range(len(PV_list)):
#         if [y_coord, x_coord] > PV_list[y_coord]:
#
#             print('X', end=' ')
#         else:
#             print('', end=' ')
#         print()
