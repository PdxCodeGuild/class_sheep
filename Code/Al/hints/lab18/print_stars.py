star_list = [[0, 0], [3, 1]]
for y_coord in range(0, 5):
    for x_coord in range(0, 5):
        if [x_coord, y_coord] in star_list:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()