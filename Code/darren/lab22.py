#lab22.py
#Computer Automated Readability Index

import string

#removes punctuation and line changes, generates a list of words
def clean_words(in_string):
    in_string = in_string.lower()
    punct = string.punctuation
    for symbol in punct:
        in_string = in_string.replace(symbol, '')
    in_string = in_string.replace('\n', ' ')
    in_string = in_string.replace('  ', ' ')
    clean_list = list(in_string.split(' '))
    return clean_list

#removes punctuation and line changes, generates a list of letters
def clean_letters(in_string):
    in_string = in_string.lower()
    punct = string.punctuation
    for symbol in punct:
        in_string = in_string.replace(symbol, '')
    in_string = in_string.replace('\n', ' ')
    in_string = in_string.replace('  ', ' ')
    clean_list = list(in_string)
    return clean_list

#removes all punctuation except periods and line changes, generates a list of sentences
def clean_sentences(in_string):
    in_string = in_string.lower()
    punct = string.punctuation
    for symbol in punct:
        if symbol != '.':
            in_string = in_string.replace(symbol, '')
    in_string = in_string.replace('\n', ' ')
    in_string = in_string.replace('  ', ' ')
    clean_list = list(in_string.split('.'))
    return clean_list

#calculates ARI as a float
def ARI_calculator(in_list):
    x = float(in_list[0])
    y = float(in_list[1])
    z = float(in_list[2])
    out_num = (4.71 * y/x) + (0.5 * x/z) - 21.43
    return out_num

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
whistle_t = file.read()
word_list = clean_words(whistle_t)
word_total = len(word_list)
letter_list = clean_letters(whistle_t)
letter_total = len(letter_list)
sentence_list = clean_sentences(whistle_t)
sentence_total = len(sentence_list)
ARIlist = [word_total, letter_total, sentence_total]
ARI = ARI_calculator(ARIlist)
ARI_round = int((ARI)+0.5)
if ARI_round > 14:
    ARI_round = 14
print(f"The ARI for this document is {ARI_round}. This corresponds to a {ari_scale[ARI_round]['grade_level']} level of difficulty, suitable for an average person of {ari_scale[ARI_round]['ages']} years old.")
