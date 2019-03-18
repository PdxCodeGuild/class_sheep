#lab5
#emojigen
import random
eye_list = ["o o", "- -", "x x", "@ @"]
nose_list = [" ,", " o", " u", " b"]
mouth_list = [" _", " v", " w", " O"]
face_no = 0
face_no = int(face_no)
while face_no < 5:
    print(random.choice(eye_list))
    print(random.choice(nose_list))
    print(random.choice(mouth_list) + '\n')
    face_no = face_no + 1
