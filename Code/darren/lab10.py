#lab10
#Average Numbers
def is_even(in_num):
    return in_num % 2 == 0
nums = []
numsum = 0
while True:
    numinput = input("Add numbers to list or type (done) >")
    if numinput == 'done':
        break
    else:
        numinput = int(numinput)
        nums.append(numinput)
nums.sort()
print(nums, end = '')
for num in nums:
    numsum = numsum + int(num)
numhalf = len(nums) // 2
nummean = numsum / len(nums)
if is_even(len(nums)):
    nummed = int(nums[numhalf]), int(nums[numhalf - 1])
else:
    nummed = nums[numhalf]
print('\n', f"Mean:{nummean}, Median:{nummed}")
# loop over the indices
#for i in range(len(nums)):
    #print(nums[i])
