
# try / except =================================================================

# 1/0 ZeroDivisionError
# ['a', 'b', 'c'].index('d') # ValueError
# 'hello'.something() # AttributeError: 'str' object has no attribute 'something'

# def get_int():
#     while True:
#         x = input('enter a number: ')
#         try:
#             x = int(x)
#             return x
#         except ValueError:
#             print('that is not a number...')
# print(get_int())



# reading files ===============================================================
# https://github.com/PdxCodeGuild/class_sheep/blob/master/1%20Python/docs/12%20-%20FileIO.md

# relative path
# file = open('../../1 Python/data/my_steps.csv')

# absolute path
# raw string, ignore escape sequences
# file = open(r'C:\Users\flux\programs\class_sheep\1 Python\data\my_steps.csv')
# text = file.read()
# print(text)

# with open('../../1 Python/data/my_steps.csv', 'r') as f:
#     text = f.read()
# print(text)

# doing http requests ==========================================================

import requests

response = requests.get('http://192.168.1.210:8000/my_steps.csv')
text = response.text

# string operations ===========================================================
# https://github.com/PdxCodeGuild/class_sheep/blob/master/1%20Python/notebooks/2-strings.ipynb

lines = text.split('\n')
lines = lines[:19] # slicing
step_records = []
for line in lines:
    line_split = line.split(',')
    d = {'date': line_split[0], 'steps': int(line_split[1])}
    step_records.append(d)

print(step_records)


total = 0
for record in step_records:
    total += record['steps']
average_steps = total/len(step_records)
print(f'Average steps: {average_steps}')

# regex =======================================================================
# https://github.com/PdxCodeGuild/class_sheep/blob/master/1%20Python/docs/Regular%20Expressions%20in%20Python.md

# import re
# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = requests.get('http://www.google.com', headers=headers)
# text = response.text
# results = re.findall(r'#[0-9a-f]{6}|#[0-9a-f]{3}', text)
# print(results)
