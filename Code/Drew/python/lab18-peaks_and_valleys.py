import random

data =[1]
up_down = [1,-1]
for i in range(1,60):
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
    water_count = 0
    for i in range(max(data), 0, -1):
        for c in range(len(data)):
            #if c == 0:
            #    if data[c] >= i:
            #        print('X', end='')
            #    else:
            #        print(' ', end='')
            #    continue
            if data[c] < i:
                if c != 0 and max(data[:c]) >= i and max(data[c:]) >=i:
                    print('o', end='')
                    water_count += 1
                else:
                    print(' ', end='')
            if data[c] >= i:
                print('X', end='')
        print()
    return water_count
print()
water_count = water(data)
print()
print(f"Amount of water: {water_count}")

#def lake_list(l):
#    lakes = []
#    for index in range(len(l)-1):
#        x = tuple(l[index])
#        lakes.append(x)
#    return lakes
#
#p_list = peaks(data)
#lakes = lake_list(p_list)
#print(lakes)
