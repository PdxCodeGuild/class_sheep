#lab21.py
#Count Words

import string

#returns the second index in a tuple
def usecount(intuple):
    return intuple[1]

#removes punctuation and line changes, generates a list
def cleantext(instring):
    instring = instring.lower()
    punct = string.punctuation
    for symbol in punct:
        instring = instring.replace(symbol, '')
    instring = instring.replace('\n', ' ')
    instring = instring.replace('  ', ' ')
    cleanlist = list(instring.split(' '))
    return cleanlist

#generates a dictionary with count of occurances in list
def dictgenerator(inlist):
    outd = {}
    for word in inlist:
        if word in outd.keys():
            outd[word] += 1
        else:
            outd[word] = 1
    return outd

#sort list according to second index using usecount function
def listsorter(indict):
    outl = []
    for key in indict:
        outl.append((key, indict[key]))
    outl= sorted(outl, key=usecount, reverse=True)
    return outl

file = open(r'/Users/pdxguest/Desktop/darrenworkingfiles/pg8486.txt')
whistlet = file.read()
whistlet = cleantext(whistlet)
whistled = dictgenerator(whistlet)
whistles = listsorter(whistled)
print(f"These are the most common ten words: {whistles[0:10]}")

pairlist = []
for item in whistles[0:10]:
    checkword = item[0]
    for index in range(len(whistlet)-1):
        if whistlet[index] == checkword:
            appendstring = whistlet[index] + ' ' + whistlet[index+1]
            pairlist.append(appendstring)
paird = dictgenerator(pairlist)
whistlep = listsorter(paird)
print(f"These are the most common ten pairs of words: {whistlep[0:10]}")
