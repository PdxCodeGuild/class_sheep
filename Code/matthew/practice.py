
import random

# problem 1 ============================================

def random_element(a):
    index = random.randint(0, len(a)-1)
    return a[index]
#
# for i in range(100):
#     fruits = ['apples', 'bananas', 'pears', 'blackberries']
#     print(random_element(fruits))


# problem 2 ============================================

def get_numbers():
    r = []
    while True:
        value = input('Enter a number (or \'done\'): ')
        if value == 'done':
            break
        value = int(value)
        r.append(value)
    return r
#
# print(get_numbers())


# problem 3 ================================================

def is_even(a):
    return a%2 == 0

def eveneven(nums):
    even_counter = 0
    for element in nums:
        if is_even(element):
            even_counter += 1
    return is_even(even_counter)
#
# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))

# problem 4 =================================================


def print_every_other_while(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 2

def print_every_other_for(nums):
    for i in range(0, len(nums), 2):
        print(nums[i])

    for i in range(len(nums)):
        if i%2 == 0:
            print(nums[i])

    for num in nums[::2]:
        print(num)

    for i in range(len(nums))[::2]:
        print(nums[i])

# print_every_other_while([1, 2, 3, 4, 5, 6, 7, 8])
# print_every_other_for([1, 2, 3, 4, 5, 6, 7, 8])



# problem 5 =================================================


# import math
# def sqrt(a):
#     return math.sqrt(a), -math.sqrt(a)
#
# root1, root2 = sqrt(4)


def reverse(nums):

    # nums.reverse()
    # return nums

    # nums = nums[::-1]
    # return nums

    # r = []
    # for num in nums:
    #     # print(num)
    #     r.insert(0, num)
    #     # print(r)
    # return r

    for i in range(len(nums)//2):
        j = len(nums)-i-1
        nums[i], nums[j] = nums[j], nums[i]

        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t
    return nums
#
# print(reverse(list(range(0, 10))))




# def edit_param(a):
#     a.append(4)
#
# a = [1, 2, 3]
# edit_param(a)
# print(a)




# problem 7 ==============================================================

def common_elements(nums1, nums2):
    common = []
    for num in nums1:
        if num in nums2 and num not in common:
            common.append(num)
        # for num2 in nums2:
        #     if num == num2:
        #         common.append(num)
    return common


print(common_elements([1, 2, 3], [2, 3, 4]))
