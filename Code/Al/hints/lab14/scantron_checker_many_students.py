# scantron_checker.py
'''
The goal of this program is to generate a students set of scantron answers, and then check them against the correct answers.
'''
import random
answers = ["a", "c", "d", "c", "b"] # the answer sheet
names = ["Sarah", "James", "Cole", "Reid"] # the students who took the test
test_dictionary = {} # it'll look like 
for name in names:
    student_guesses = []
    for num in range(5): # for num in [0, 1, 2, 3, 4]
        student_guesses.append(random.choice(options)) # each student guessed randomly
    test_dictionary[name] = student_guesses
print(test_dictionary)

# for active_student in test_dictionary.keys():
for active_student in names:
    correct_answers = 0
    for question_num in range(5): # for question_num in [0, 1, 2, 3, 4]
        if answers[question_num] == test_dictionary[active_student][question_num]: # check student's first answer against correct first answer, etc.
            correct_answers += 1 # it's correct, so add one to correct answers
    print(f"{active_student} got {correct_answers} answers correct.")
