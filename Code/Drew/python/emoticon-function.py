#sheep themed
import random

# Set body parts for the sheep
def funcsheep(x):
    eye = ['･','ᵒ','ºั','♥','Ꮎ','o','x','ಠ','ᵔ','ô','▰','⨂','◕','❂','Ծ','Θ','◉']
    mouth = ['ꈊ','^','-','_','౪','益','▽','ಟ','o','O','⌂','◡']
    i = 0
    while i < x:
        eye_match = random.choice(eye)
        print('\n                   (\___/)\n        @@@@@@@@@@@| '+eye_match+'  '+eye_match+'|\n     @@@@@@@@@@@@@@\     /\n    @@@@@@@@@@@@@@@@\ '+random.choice(mouth)+' /\n    @@@@@@@@@@@@@@@@@\_/\n     @@@@@@@@@@@@@@@\n       ||        ||\n       ~~        ~~\n')
        i += 1

sheep = int(input('How many sheep do you want?\n'))
funcsheep(sheep)
