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

input_url = input("Type 'd' to load sample text, OR \nEnter a URL:\n")
if input_url == 'd':
    print("Dracula by Bram Stoker")
    input_url = 'http://www.gutenberg.org/cache/epub/345/pg345.txt'
r = requests.get(input_url)
sample_text = r.text


def char_count(t):
    char_list = re.findall("(\w)", t)
    return len(char_list)

def word_count(t):
    word_list = re.findall("(\S+)", t)
    return len(word_list)

def sentence_count(t):
    sentence_list = re.findall("()([\.\?!][\'\"\u2018\u2019\u201c\u201d\)\]]*\s*(?<!\w\.\w.)(?<![A-Z][a-z][a-z]\.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)\s+)", t)
    return len(sentence_list)

def roundup(x):
    return round(x+.5)

ari = roundup((4.71*(char_count(sample_text)/word_count(sample_text)))+(0.5*(word_count(sample_text)/sentence_count(sample_text)))-21.43)
if ari > 14:
    ari = 14

print(f"The ARI for this text is {ari}")
print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")
