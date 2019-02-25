#emojigen
import random
eyelist = ["o o", "- -", "x x", "@ @"]
noselist = [" ,", " o", " u", " b"]
mouthlist = [" _", " v", " w", " O"]
faceno = 0
faceno = int(faceno)
while faceno < 5:
    print(random.choice(eyelist))
    print(random.choice(noselist))
    print(random.choice(mouthlist))
    faceno = faceno + 1
