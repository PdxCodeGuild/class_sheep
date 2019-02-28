# version 2
nums = []
while True:
    user_nums = input("enter a number (or 'done' if done):")
    if user_nums == 'done':
        break
    else:
        nums.append(int(user_nums))
added = 0
for num in nums:
    added += num
    average = added/(len(nums))
print(average)
