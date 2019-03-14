#lab22.py
#Computer Automated Readability Index

import string

#removes punctuation and line changes, generates a list of words
def cleanwords(instring):
    instring = instring.lower()
    punct = string.punctuation
    for symbol in punct:
        instring = instring.replace(symbol, '')
    instring = instring.replace('\n', ' ')
    instring = instring.replace('  ', ' ')
    cleanlist = list(instring.split(' '))
    return cleanlist

#removes punctuation and line changes, generates a list of letters
def cleanletters(instring):
    instring = instring.lower()
    punct = string.punctuation
    for symbol in punct:
        instring = instring.replace(symbol, '')
    instring = instring.replace('\n', ' ')
    instring = instring.replace('  ', ' ')
    cleanlist = list(instring)
    return cleanlist

#removes all punctuation except periods and line changes, generates a list of sentences
def cleansentences(instring):
    instring = instring.lower()
    punct = string.punctuation
    for symbol in punct:
        if symbol != '.':
            instring = instring.replace(symbol, '')
    instring = instring.replace('\n', ' ')
    instring = instring.replace('  ', ' ')
    cleanlist = list(instring.split('.'))
    return cleanlist

#calculates ARI as a float
def ARIcalc(inlist):
    x = float(inlist[0])
    y = float(inlist[1])
    z = float(inlist[2])
    outnum = (4.71 * y/x) + (0.5 * x/z) - 21.43
    return outnum

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

file = open(r'/Users/pdxguest/Desktop/darrenworkingfiles/pg8486.txt')
whistlet = file.read()
wordlist = cleanwords(whistlet)
wordtotal = len(wordlist)
letterlist = cleanletters(whistlet)
lettertotal = len(letterlist)
sentencelist = cleansentences(whistlet)
sentencetotal = len(sentencelist)
ARIlist = [wordtotal, lettertotal, sentencetotal]
ARI = ARIcalc(ARIlist)
ARIround = int((ARI)+0.5)
if ARIround > 14:
    ARIround = 14
print(f"The ARI for this document is {ARIround}. This corresponds to a {ari_scale[ARIround]['grade_level']} level of difficulty, suitable for an average person of {ari_scale[ARIround]['ages']} years old.")
