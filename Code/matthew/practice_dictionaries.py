

# problem 1 ====================================================



# nums = []
# nums[0] = 55 # crash


def combine(keys, values):
    fruit_dictionary = {}
    # ??
    # fruit_dictionary['peach'] = 5.5

    # for x in fruit_dictionary:
    #     print(f'fruit_dictionary[{x}] = {fruit_dictionary[x]}')

    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        fruit_dictionary[key] = value

    return fruit_dictionary

#             0       1         2
fruits = ['apple', 'banana', 'pear']
prices = [    1.2,      3.3,    2.1]
print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}
