
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

import statistics
nums_list = []
user_input = input("enter a number, or 'done': ")
while user_input != 'done':
    nums_list.append(int(user_input))
    user_input = (input("enter a number, or 'done': "))


count = 0
for number in nums_list:
        count += number

print(f"total numbers equals {count}")

nums_list_sorted = (list(sorted(nums_list)))

print((nums_list_sorted))

print(f"this is the median {statistics.median(nums_list)}")
# nums_list_sorted = nums_list_sorted.append(1)
# return_value = nums_list_sorted.pop(int(count/2))
# print(f"return value {return_value}")



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
