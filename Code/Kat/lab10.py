# Lab 10: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

nums = [5, 0, 8, 3, 4, 1, 6]
added = 0
for num in nums:
    added += num
average = added/len(nums)
print(f"The average is {average}.")

# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average.

nums = []
print("This program checks the mean (average) of any list of numbers.")
while True:
    user_nums = input("Enter any number (or 'done' if done):")
    if user_nums == 'done':
        break
    nums.append(int(user_nums))
added = 0
for num in nums:
    added += num
    average = added/len(nums)
print(f"The mean is {average}.")


# Version 3
# Calculate the median. The median is the number in the middle when the list is sorted. If there's an even number of numbers, the median is a list of the two numbers in the middle. Remember the sort method on lists.

nums = []
print("This program checks the median of any list of numbers.")
while True:
    user_nums = input("Enter any number (or 'done' if done): ")
    if user_nums == 'done':
        break
    nums.append(int(user_nums))
# put the numbers in order from smallest to largest
nums.sort()
# if there is an odd number of numbers, there is one median
if len(nums) % 2 == 1:
    print(f"The median is {nums[len(nums)//2]}.")
# if there is an even number or numbers, there will be two medians
if len(nums) % 2 == 0:
    print(f"The medians are {nums[len(nums)//2]} and {nums[len(nums)//2 - 1]}.")
