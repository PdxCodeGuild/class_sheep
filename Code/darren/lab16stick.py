#lab16stick.py
'''Pillow (Stick Figure Version)'''

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0,0), (width, height)), fill="white")

draw.rectangle(((225, 275), (275, 125)), fill="lightgreen")

draw.line((275, 375, width, height), fill="lightgreen")
draw.line((0, height, 225, 375), fill = "lightgreen")

draw.rectangle(((150, 175), (350, 200)), fill="lightgreen")
color = (256, 128, 128)

draw.rectangle(((225, 200), (245, 375)), fill="lightgreen")

draw.rectangle(((255, 200), (275, 375)), fill="lightgreen")

circle_x = width/2
circle_y = height/4
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightblue')

circle_x = width/2.1
circle_y = height/4.5
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

circle_x = width/1.9
circle_y = height/4.5
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

circle_x = width/2
circle_y = height/3.5
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

img.show()
#
# from PIL import Image, ImageDraw
# from random import randint
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(img)
#
# for i in range(1000):
#     x0 = randint(0, width)
#     y0 = randint(0, height)
#     x1 = randint(0, width)
#     y1 = randint(0, height)
#     line_width = randint(1, 40)
#     red = randint(0, 255)
#     green = randint(0, 255)
#     blue = randint(0, 255)
#     draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)
#
# img.show()
