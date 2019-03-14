#lab21.py
#Count Words
def usecount(intuple):
    return intuple[1]

import string
file = open(r'/Users/pdxguest/Desktop/darrenworkingfiles/pg8486.txt')
whistletxt = file.read()
whistletxt = whistletxt.lower()
symbolstring = string.punctuation
mystring = 'Yo.Buddy'
mystring = mystring.lower()
for symbol in symbolstring:
    whistletxt = whistletxt.replace(symbol, '')
whistletxt = whistletxt.replace('\n', ' ')
whistledict = {}
whistletxt = list(whistletxt.split(' '))
for word in whistletxt:
    if word in whistledict.keys():
        whistledict[word] += 1
    else:
        whistledict[word] = 1
sorterlist = []
for key in whistledict:
    sorterlist.append((key, whistledict[key]))
sorterlist= sorted(sorterlist, key=usecount, reverse =True)
print(sorterlist[0:10])
