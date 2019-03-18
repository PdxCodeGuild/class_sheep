import re
import requests

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

input_url = input('Enter a URL:\n')
r = requests.get(input_url)
sample_text = r.text

title = sample_text.split('\n', 1)[0]

def wordcount(t):
    word_list = re.findall("(\S+)", t)
    return len(word_list)

def wwordcount(t):
    word_list = re.findall("(\w)", t)
    return len(word_list)

def swordcount(t):
    word_list = re.findall("(\S)", t)
    return len(word_list)

def pwordcount(t):
    word_list = re.findall("(\w+)", t)
    return len(word_list)

def wlist(t):
    word_list = re.findall("(\w+)", t)
    return word_list

def slist(t):
    word_list = re.findall("(\S+)", t)
    return word_list

def roundup(x):
    return round(x+.5)

print(f"\\S+ - {wordcount(sample_text)}")
print(f"\\w - {wwordcount(sample_text)}")
print(f"\\S - {swordcount(sample_text)}")
print(f"\\w+ - {pwordcount(sample_text)}")

for i in range(20):
    print(wlist(sample_text)[i])

for i in range(20):
    print(slist(sample_text)[i])

#print(f"The ARI for {title} is {}")
#print(f"This corresponds to a {} level of difficulty")
#print(f"that is suitable for an average person {} years old.")
