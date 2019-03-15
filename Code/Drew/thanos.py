import os
import random
import time

# This creates a list of all files in current directory and subdirectory
file_list = []
for subdir, dirs, files in os.walk('./'):
    for file in files:
        if 'thanos' in file:
            continue
        else:
            file_list += [os.path.join(subdir,file)]

# A function to randomly select half of the input variable
def condemn(population):
    unlucky = random.sample(population, len(population)//2+1)
    return unlucky

snap = condemn(file_list)

# This function deletes all files in the given list, with a little verbosity
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
