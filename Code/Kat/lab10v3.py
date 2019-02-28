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
