import random
eye_list = ['8',':',';','B']
nose_list = ['>','V']
mouth_list = [')','p','O']
i = 0
while i < 5:
    i += 1
    eyes = random.choice(eye_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list)

    print(f'{eyes}{nose}{mouth}')
