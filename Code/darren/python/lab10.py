#lab10.py
'''Average Numbers'''

'''Determines if number is even'''
def is_even(in_num):
    return in_num % 2 == 0

nums = []
num_dict = {}
num_sum = 0
num_freq = 0
num_mode = ''
num_mode_too = ''
while True:
    num_input = input("Add numbers to list or type (done) >")
    if num_input == 'done':
        break
    num_input = int(num_input)
    nums.append(num_input)
    if num_input in num_dict.keys():
        num_dict[num_input] += 1
    else:
        num_dict[num_input] = 1
nums.sort()
print(nums, end = '')
for num in nums:
    num_sum = num_sum + int(num)
num_half = len(nums) // 2
num_mean = num_sum / len(nums)
if is_even(len(nums)):
    num_med = int(nums[num_half]), int(nums[num_half - 1])
else:
    num_med = nums[num_half]
for num_val in num_dict.keys():
    if num_dict[num_val] > num_freq:
        num_freq = num_dict[num_val]
        num_mode = num_val
        num_mode_too = ''
    if num_dict[num_val] == num_freq and num_mode != num_val:
        num_mode_too += (' ' + str(num_val))
# for num_val in num_dict.keys():
#     if num_dict[num_val] > num_freq:
#         num_freq = num_dict[num_val]
#         num_mode = num_val
# #         num_mode_too = ''
# #     if num_dict[num_val] == num_freq and num_mode != num_val:
# #         num_mode_too += (' ' + str(num_val))
print('\n', f"Mean:{num_mean}, Median:{num_med}, Mode:{num_mode}{num_mode_too}, {num_freq} times)")
