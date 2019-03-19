import string
import re
with open('dr_fu_manchu.txt', 'r') as f:
    text = f.read()

text = re.sub(r'Dr\.|Mr\.|Ms\.|[A-Z]\.|Mrs\.|\.net|\.org|\.com|\.gov|http:|\/|www\.',r'', text)
text = re.sub(r'\!|\?', r'\.', text)

# text = text.lower()
text = text.strip()

#================================================================
#Average characters per word
text_list = text.split()
total_words = len(text_list)

#length list will determine the length of every word in the text
length_list = []
for i in range(len(text_list)):
    length_list.append(len(text_list[i]))
#total_characters sums up all the character values in length list
total_characters = 0
for i in range(len(length_list)):
    total_characters += length_list[i]
#average is the total characters divided by total words

average_cw = total_characters/total_words



#================================================================
#Average words per sentence

#Removes the white space from the text, including \n.  replaces it with ''.
text = re.sub(r'\s', r'', text)

#Transforms string into list of strings
sentence_list = text.split('.')

#This is a counter for the total number of strings.  the for loop iterates over each indice.  each indicie should be a sentence.  The goal is to find the words per sentence
total_sentences = 0
for i in range(len(sentence_list)):
    total_sentences += 1
words_per_sentence = (total_words/total_sentences)

#inputing the average characters per word and words per sentence into the ari formula, we can calculate ARI.  the if statement is used to determine if there is a remainder.  if there is a remainder we 'round-up' and then remove the decimal so that the ari can be used as a key in the ari_scale.
ari = ((4.71*average_cw)+(.5* words_per_sentence) - 21.43)
if ari % 1 > 0:
    ari += 1
    ari = int(round(ari,0))


#==================================================================
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
# print(ari_scale[ari]['ages'])
print(f"The ARI for The Insidious Dr. Fu Manchu is {ari}.  This corresponds to {ari_scale[ari]['grade_level']} reading and is suitable for an average age of  {ari_scale[ari]['ages']} years old")
