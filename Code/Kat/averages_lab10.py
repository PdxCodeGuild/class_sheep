# version 1
# nums = [5, 0, 8, 3, 4, 1, 6]
# added = 0
# for num in nums:
#     added += num
# average = added/(len(nums))
# print(average)

#version 2
# user_nums = input("Enter a number of press 'done' when finished. >")
# in_list = []
# while True:
#     user_nums = input("Enter a number of press 'done' when finished. >")
#     if user_nums == 'done':
#         break
#     else:
#         in_list = in_list.append(float(user_nums))
#         for user_nums in range(len(user_nums)):
#
# added = 0
# for num in in_list:
#     added += num
# average = added/(len(nums))
# print(average)

# version 2
# nums = []
# while True:
#     user_nums = input("enter a number (or 'done' if done):")
#     if user_nums == 'done':
#         break
#     else:
#         nums.append(int(user_nums))
# added = 0
# for num in nums:
#     added += num
#     average = added/(len(nums))
# print(average)


# version 3
nums = []
while True:
    user_nums = input("enter a number (or 'done' if done):")
    if user_nums == 'done':
        break
    else:
        nums.append(int(user_nums))
nums.sort()
if len(nums) % 2 == 1:
    print(nums[len(nums)//2])
if len(nums) % 2 == 0:
    print(nums[len(nums)//2])
    print(nums[(len(nums)//2) - 1])
