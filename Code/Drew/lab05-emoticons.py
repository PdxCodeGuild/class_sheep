#sheep themed
import random

eye = ['･','ᵒ','ºั','♥','Ꮎ','o','x','ಠ','ᵔ','ô','▰','⨂','◕','❂','Ծ','Θ','◉','〠']
mouth = ['ꈊ','^','-','_','౪','益','▽','ಟ','o','O','⌂','◡']
i = 0
while i < 5:
    eye_match = random.choice(eye)
    print('\n                   (\___/)\n        @@@@@@@@@@@| '+eye_match+'  '+eye_match+'|\n     @@@@@@@@@@@@@@\     /\n    @@@@@@@@@@@@@@@@\ '+random.choice(mouth)+' /\n    @@@@@@@@@@@@@@@@@\_/\n     @@@@@@@@@@@@@@@\n       ||        ||\n       ~~        ~~\n')
    i += 1
