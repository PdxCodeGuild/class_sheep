import requests
import math
import string
#http request for Mary Shelley's Frankenstein
response = requests.get('http://www.gutenberg.org/files/84/84-0.txt')
text = response.text
#Getting rid of double spaces
text = text.replace('  ', ' ')

#function counting characters (as defined in the official ARI scale as letters and numbers)
def count_characters(text):
    character_counter = 0
    for character in text:
        if character in string.ascii_letters or character in string.digits:
            character_counter += 1
    return character_counter

#function counting words (as defined in the offical ARI scale as spaces)
def count_words(text):
    text = text.replace('—', ' ')
    text = text.replace('-', ' ')
    text = text.split()
    return len(text)

#function counting sentences (this is done manually in the official ARI scale calculations but in this case is based on punctuation)
def count_sentences(text):
    text = text.replace('...', '.')
    text = text.replace('Mr.', 'Mr')
    text = text.replace('Mrs.', 'Mrs')
    text = text.replace('Ms.', 'Ms')
    text = text.replace('Dr.', 'Dr')
    sentence_counter = 0
    for character in text:
        if character == '.' or character == '!' or character == '?':
            sentence_counter += 1
    return sentence_counter

#function calculating ARI based on above counts and rounding up (per instructions)
def find_ari(text):
    first_step = 4.71 * (count_characters(text)/count_words(text))
    second_step = 0.5 * (count_words(text)/count_sentences(text)) - 21.43
    return math.ceil(first_step + second_step)

#provided dictionary of ARI scale results and corresponding levels
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

demographics = ari_scale[find_ari(text)]

print(f"The ARI for Mary Shelley's Frankenstein is {find_ari(text)}. This corresponds to ages {demographics['ages']} or {demographics['grade_level']}.")
