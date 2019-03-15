import os
import random
import time

file_list = []
for subdir, dirs, files in os.walk('./'):
    for file in files:
        if 'thanos' in file:
            continue
        else:
            file_list += [os.path.join(subdir,file)]
            #file_list.append(subdir+file)

def condemn(population):
    unlucky = random.sample(population, len(population)//2+1)
    return unlucky

snap = condemn(file_list)

def gauntlet(var):
    for file in var:
        os.remove(file)

def thanos(dir):
    for n in range(3):
        time.sleep(1)
        print('.', end='', flush=True)
    print()
    print("Your files don't feel so good", end='')
    for n in range(3):
        time.sleep(1)
        print('.', end='', flush=True)
    time.sleep(1)
    print()
    time.sleep(1)
    for file in dir:
        time.sleep(.1)
        print(f"deleting: {file}")
        os.remove(file)
    print()
    time.sleep(2)
    print("Perfectly Balanced.")
    time.sleep(2)
    print()

thanos(snap)
