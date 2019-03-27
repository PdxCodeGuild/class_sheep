import time
import os

def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

size = int(input("Enter a number:\n"))
fiblist = fibonacci(size)
clear = lambda: os.system('clear')
clear()
for i in range(len(fiblist)):
    print(fiblist[i])
    time.sleep(.2)
