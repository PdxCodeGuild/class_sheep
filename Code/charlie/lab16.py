
# #V1 using pillow (which is in integers)
# from PIL import Image
# import colorsys
#
# img = Image.open("rainbow.jpg") # must be in same folder
# width, height = img.size
# pixels = img.load()
#
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         Y = round(0.299*r + 0.587*g + 0.114*b)
#         pixels[i, j] = (Y, Y, Y)
# img.show()

#V2 using colorsys (which is in floats)

# from PIL import Image
# import colorsys
#
# img = Image.open("rainbow.jpg") # must be in same folder
# width, height = img.size
# pixels = img.load()
#
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
#         h = float(r/255) +.4
#         s = float(g/255) - .2
#         v = float(b/255) + .1
#
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#
#
#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)
#
#         pixels[i, j] = (r, g, b)
#         # Y = round(0.299*r + 0.587*g + 0.114*b)
#         # pixels[i, j] = (Y, Y, Y)
# img.show()

#V3 Drawing

# from PIL import Image, ImageDraw
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
#
# draw = ImageDraw.Draw(img)
#
#
# # the origin (0, 0) is at the top-left corner
#
# draw.rectangle(((0, 0), (width, height)), fill="white")
#
# # draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (50, 50)), fill="lightblue")
#
# # draw a line from x0, y0, x1, y1
# # using the color pink
# color = (256, 128, 128)  # pink
# draw.line((250, 200, 400, 100), fill=color)#left arm
# draw.line((250, 200, 100, 100), fill=color)#right arm
# draw.line((250,100, 250, 400), fill = color) #body
# draw.line((250, 400, 350, 450), fill=color)#left leg
# draw.line((350, 450, 400, 400), fill=color)
# draw.line((250, 400, 100, 500), fill = color) #right leg
# circle_x = width/2
# circle_y = height/5
# circle_radius = 50
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
#
# img.show()

#v4

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()
