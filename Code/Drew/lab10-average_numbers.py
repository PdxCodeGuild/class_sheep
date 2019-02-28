import string

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
#
#print(count_dict)
#highest = max(set(nums), key=nums.count)
#print(highest)
#mode = []
#for number, occurence in count_dict.items():
#    if occurence == highest:
#        mode.append(number)
#print(mode)
#print(max(nums))
#print(nums)
#print(sum(nums))
avg = sum(nums)/len(nums)
print(f"The average is {avg}.")
mode = []
counts = list(count_dict.items())
counts.sort(key=lambda tup: tup[1], reverse=True)
highest = counts[0][1]
for number, occurence in counts:
    if occurence == highest:
        mode.append(number)
print(f"The mode or modes is/are {mode}")
