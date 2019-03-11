import random

data =[1]
up_down = [1,-1]
for i in range(1,80):
    if data[i-1] > 0:
        data.append(data[i-1]+random.choice(up_down))
    else:
        data.append(1)

def peaks(l):
    p_list = []
    for i in range(1,len(l)-1):
        if l[i-1] < l[i] and l[i+1] < l[i]:
            p_list.append(i)
    return p_list

def valleys(l):
    v_list = []
    for i in range(1,len(l)-1):
        if l[i-1] > l[i] and l[i+1] > l[i]:
            v_list.append(i)
    return v_list

def peaks_and_valleys(l):
    pv_list = []
    for x in peaks(l):
        pv_list.append(x)
    for x in valleys(l):
        pv_list.append(x)
    pv_list.sort()
    return pv_list

print("Data:")
print(data)
print("Peaks:")
print(peaks(data))
print("Valleys:")
print(valleys(data))
print("Peaks and Valleys:")
print(peaks_and_valleys(data))

def xdraw(l):
    for i in range(max(data), 0, -1):
        for c in range(len(data)):
            if data[c] < i:
                print(' ', end='')
            if data[c] >= i:
                print('X', end='')
        print()

xdraw(data)

def water(l):
    for i in range(max(data), 0, -1):
        for c in range(len(data)):
            if data[c] < i:
                #if data[c-1] >= i and max(data[c:]) >=i:
                    #print('o', end='')
                try:
                    if max(data[1:c]) >= i and max(data[c:]) >=i:
                        print('o', end='')
                    else:
                        print(' ', end='')
                except ValueError:
                    print(' ',end='')
            if data[c] >= i:
                print('X', end='')
        print()
print()
water(data)
