#lab10
#Average Numbers
def is_even(in_num):
    return in_num % 2 == 0
nums = []
numdict = {}
numsum = 0
numfreq = 0
nummode = ''
nummodetoo = ''
while True:
    numinput = input("Add numbers to list or type (done) >")
    if numinput == 'done':
        break
    else:
        numinput = int(numinput)
        nums.append(numinput)
        if numinput in numdict.keys():
            numdict[numinput] += 1
        else:
            numdict[numinput] = 1
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
for numval in numdict.keys():
    if numdict[numval] > numfreq:
        numfreq = numdict[numval]
        nummode = numval
        nummodetoo = ''
    if numdict[numval] == numfreq and nummode != numval:
        nummodetoo += (' ' + str(numval))
# for numval in numdict.keys():
#     if numdict[numval] > numfreq:
#         numfreq = numdict[numval]
#         nummode = numval
# #         nummodetoo = ''
# #     if numdict[numval] == numfreq and nummode != numval:
# #         nummodetoo += (' ' + str(numval))
print('\n', f"Mean:{nummean}, Median:{nummed}, Mode:{nummode}{nummodetoo}, {numfreq} times)")
