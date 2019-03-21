# Lab 22: Compute Automated Readability Index

import string
letters = []

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

with open("the_adventures_of_reddy_fox.txt", encoding="utf-8") as f:
    book = f.read().lower()

book_title = 'the_adventures_of_reddy_fox.txt'

period_count = book.count('.')
exclamation_count = book.count('!')
question_count = book.count('?')

punctuation_counter = period_count + exclamation_count + question_count

for punctuation in string.punctuation: # remove ALL punctuation
    book = book.replace(punctuation, '')

book_list = book.split() # split the string of words into a list of words where each word is a list item

word_count = len(book_list) #count the number of words in the book

for i in range (len(book_list)): #find the number of individual letters in the book
    for char in range(len(book_list[i])):
        letters.append(book_list[i][char])

char_count = len(letters) #count the number of letters in the book

ari_score = ((4.71 * (char_count / word_count) + (0.5 * (word_count / punctuation_counter)) - 21.43)) #calculate ari score

#if the score is greater than 14, age and grade level = score
if ari_score > 14:
    ari_score = 14

rounded_score = round(ari_score)

ari_age = ari_scale[rounded_score]

print('-' * 60)
print(f'The ARI score for {book_title} is {rounded_score}.')
print('This corresponds to a ' + ari_age['grade_level'] + ' reading level \nthat is suitable for an average person ' + ari_age['ages'] + ' years old.')
print('-' * 60)
