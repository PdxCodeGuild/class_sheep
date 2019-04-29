import re
import string
with open('dr_fu_manchu.txt', 'r') as f:
    text = f.read()
# results = re.findall(r'Dr\.|Mr\.|Ms\.|[A-Z]\.|Mrs\.|\.net|\.org|\.com|\.gov|http:|\/|www\.', text)

text = re.sub(r'Dr\.|Mr\.|Ms\.|[A-Z]\.|Mrs\.|\.net|\.org|\.com|\.gov|http:|\/|www\.',r'', text)
text = re.sub(r'\!|\?', r'\.', text)
print(text)

text.find(!)
