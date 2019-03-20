# scantron_checker_one_student.py
'''
The goal of this program is to generate a students set of scantron answers, and then check them against the correct answers.
'''
import random
options = ["a", "b", "c", "d"]
answers = ["a", "c", "d", "c", "b"] # the answer sheet
reid_answers = []
for num in range(0, 5): # for num in [0, 1, 2, 3, 4]
    reid_answers.append(random.choice(options)) # reid guessed randomly
print(f"The answers are {answers}")
print(f"Reid guessed {reid_answers}")
correct_answers = 0
# for num in range(len(answers)):
for num in range(0, 5): # for num in [0, 1, 2, 3, 4]
    if reid_answers[num] == answers[num]: # check reid's first answer against correct first answer, etc.
        correct_answers += 1 # it's correct, so add one to correct answers
print(f"{correct_answers} correct answers!")
