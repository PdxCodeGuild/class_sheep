# Lab 18 - Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#write a function to check for peaks and valleys

def peaks(left, middle, right):
    if middle > left and middle > right:
        return True
    else:
        return False

def valleys(left, middle, right):
    if middle < left and middle < right:
        return True
    else:
        return False

for index in range(1, len(data) -1):
    if peaks(data[index - 1], data[index], data[index +1]):
        print(f'Peak at {index}')
    elif valleys(data[index - 1], data[index], data[index +1]):
        print(f'Valley at {index}')
