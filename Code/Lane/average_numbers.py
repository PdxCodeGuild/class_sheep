version 1

nums = [5, 0, 8, 3, 4, 1, 6]
counter = 0
for n in nums:
    counter += n

average = counter/len(nums)
print('The average of these numbers is: ', average)


#
# #version 2
#
# user_numbers = []
#
# while True:
#
#     user_input = input("Enter a number to continue or done to quit: ")
#     if user_input == 'done':
#         break
#     user_input = int(user_input)
#     user_numbers.append(user_input)
#
# print("average = ", sum(user_numbers) / len(user_numbers))
#
#
# #version 3
# nums = []
#
# while True:
#     user_input = input("Enter a number to continue or done to quit: ")
#     if user_input == 'done':
#         break
#     else:
#         user_input = int(user_input)
#         nums.append(user_input)
#
# length = len(nums)
# nums.sort()
#
# if length % 2 == 0:
#     print(nums[len(nums) // 2 - 1], nums[len(nums) // 2])
# else:
#     print(nums[len(nums) // 2])
