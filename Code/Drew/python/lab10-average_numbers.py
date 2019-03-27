import string

# get user input
nums = []
while True:
    entry = input("Enter a number, or type 'done':\n")
    if entry in ["done"]:
        break
    else:
        try:
            nums.append(int(entry))
        except ValueError:
            print("Please enter a number")
        continue
count_dict = {}
for i in nums:
    count_dict[i] = count_dict.get(i, 0) + 1

# sort list
nums = sorted(nums)

# print length, sum, avg
print(f"You entered {len(nums)} numbers.")
print(f"The total sum is {sum(nums)}.")
avg = sum(nums)/len(nums)
print(f"The average is {avg}.")

# calculate median
if len(nums)%2 == 1:
    print(f"The median is {nums[int(len(nums)/2)]}.")
elif len(nums)%2 == 0 :
    if nums[int(len(nums)/2)-1] == nums[int(len(nums)/2)]:
        print(f"The median is {nums[int(len(nums)/2)]}.")
    else:
        print(f"The medians are {nums[int(len(nums)/2)-1]} and {nums[int(len(nums)/2)]}.")


# calculate mode
mode = []
counts = list(count_dict.items())
counts.sort(key=lambda tup: tup[1], reverse=True)
highest = counts[0][1]
for number, occurence in counts:
    if occurence == highest:
        str(number)
        mode.append(number)
if len(mode) == 1:
    print(f"The mode is {mode}.")
elif len(mode) > 1:
    modestring = ",".join(str(x) for x in mode[:-1])
    print(f"The modes are {modestring} and {mode[-1]}.")
