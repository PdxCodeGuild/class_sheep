# print_board.py

list_of_lists = []

symbol_list = ['.', 'x', 'X', 'hi']

for index1 in range(3):
    temp_list = []
    for index2 in range(3):
        # temp_list.append(symbol_list[index1])
        temp_list.append(symbol_list[index2])
    list_of_lists.append(temp_list)

for small_list in list_of_lists:
	print(small_list)
