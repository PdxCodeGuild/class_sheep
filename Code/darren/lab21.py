#lab21.py
#Count Words
def usecount(intuple):
    return intuple[1]

import string
file = open(r'/Users/pdxguest/Desktop/darrenworkingfiles/pg8486.txt')
whistlet = file.read()
whistlet = whistlet.lower()
punct = string.punct
mystring = 'Yo.Buddy'
mystring = mystring.lower()
for symbol in punct:
    whistlet = whistlet.replace(symbol, '')
whistlet = whistlet.replace('\n', ' ')
whistled = {}
whistlet = list(whistlet.split(' '))
for word in whistlet:
    if word in whistled.keys():
        whistled[word] += 1
    else:
        whistled[word] = 1
whistles = []
for key in whistled:
    whistles.append((key, whistled[key]))
whistles= sorted(whistles, key=usecount, reverse =True)
print(whistles[0:10])
