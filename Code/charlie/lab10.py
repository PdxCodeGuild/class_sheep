
# V1
# nums_list = [5, 0, 8, 3, 4, 1, 6]
# count = 0
# for number in nums_list:
#         count += number
# print(count)
#
# length = len(nums_list)
# print(length)
#
# average = (count/length)
# print(average)

#V2
# nums_list = []
# user_input = input("enter a number, or 'done': ")
# while user_input != 'done':
#     nums_list.append(int(user_input))
#     user_input = (input("enter a number, or 'done': "))
#
#
# count = 0
# for number in nums_list:
#         count += number
# print(f"total numbers equals {count}")
#
# length = len(nums_list)
# print(f"numbers in list {length}")
#
# average = (count/length)
# print(f"average numbers {average}")

#V3

# import statistics
# nums_list = []
# user_input = input("enter a number, or 'done': ")
# while user_input != 'done':
#     nums_list.append(int(user_input))
#     user_input = (input("enter a number, or 'done': "))
#
#
# count = 0
# for number in nums_list:
#         count += number
#
# print(f"total numbers equals {count}")
#
# nums_list_sorted = (list(sorted(nums_list)))
#
# print((nums_list_sorted))
#
# print(f"this is the median {statistics.median(nums_list)}")
# print(f"this is the mediam manually computed {nums_list_sorted[((len(nums_list_sorted)//2))]}")
#
# print(f"return value {nums_list_sorted}")


#4

import statistics
nums_list_dict = {}
while True:
    user_input = input("enter a number, or 'done': ")
    if user_input == "done":
        break
    if user_input in nums_list_dict.keys():
        nums_list_dict[user_input] += 1
    else:
        nums_list_dict[user_input] = 1
    print(nums_list_dict)

biggest_num = 0
biggest_num_mode = 0
for number in nums_list_dict:
    if nums_list_dict[number] > biggest_num:
        biggest_num = nums_list_dict[number]
        biggest_num_mode = number
print(f"the mode is {biggest_num_mode}")
# count = 0
# for number in nums_list_dict:
#         count += number
#
# print(f"total numbers equals {count}")
#
# nums_list_sorted_dict = (list(sorted(nums_list_dict)))
#
# print((nums_list_sorted_dict))
#
# print(f"this is the mode {statistics.mode(nums_list_dict)}")

# print(f"return value {nums_list_sorted_dict}")

#to find the median, refer to is_even_funtion



# nums_list_sorted=int(''.join(nums_list_sorted) for number in nums_list_sorted)
# print(int_num_list)
# print(f"this is the median calcuated manually {nums_list_sorted}")



# length = len(nums_list)
# print(f"numbers in list {length}")
#
# average = (count/length)
# print(f"average numbers {average}")





# length = len(nums_list)
# addition = sum(nums_list)
# average = addition/length
# print(average)

# def positive_number(nums_list):
#     if nums_list > 0:
#         return True
#     else:
#         return False
#
# for number in nums_list:
#     print(number)
#
# positive_number(number)
