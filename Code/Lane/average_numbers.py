nums = [5, 0, 8, 3, 4, 1, 6]
counter = 0
for n in nums:
    counter += n

average = counter/len(nums)
print('The average of these numbers is: ', average)



#version 2

user_numbers = []

while True:

    user_input = input("Enter a number to continue or done to quit: ")
    if user_input == 'done':
        break
    user_input = int(user_input)
    user_numbers.append(user_input)

print(sum(user_numbers) / len(user_numbers))
