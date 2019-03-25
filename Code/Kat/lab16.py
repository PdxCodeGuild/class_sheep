# Lab 16: Image Manipulation
# Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'. First download the file from here and place it in the same directory as your code (or save it anywhere and use an absolute path when opening it). If you don't have pillow installed, run pip install pillow in a terminal. You can check if pillow using pip show pillow.
#
# Use the formula for converting to greyscale and the code below. Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.

# version 1, make greyscale
from PIL import Image
import colorsys
img = Image.open("hqdefault.jpg")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = round(0.299*r + 0.587*g + 0.114*b)
        pixels[i, j] = (Y, Y, Y)
img.show()

# version 2, increase saturation (replace += with -= to decrease saturation)
img = Image.open("hqdefault.jpg")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if 0.5 < h < 0.7:
            h += 0.2
        if 0.5 < s < 0.7:
            s += 0.2
        if 0.5 < v < 0.7:
            v += 0.2

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)
img.show()

# Version 2
# Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue. Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255. You'll have to convert between these two representations.

from PIL import Image
import colorsys
img = Image.open("hqdefault.jpg")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if h > 0.3:
            h = s + 0.2
        if s > 0.3:
            s = v + 0.2
        if v > 0.3:
            v = h + 0.2

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)
img.show()


from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# Version 3
# Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. Use these functions to draw a stick figure.

# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((200, 200), (300, 400)), fill="black")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((100, 250, 200, 250), fill=color)
draw.line((400, 250, 300, 250), fill=color)
draw.line((250, 150, 250, 200), fill=color)
draw.line((150, 500, 225, 400), fill=color)
draw.line((350, 500, 275, 400), fill=color)


circle_x = width/2
circle_y = height/4
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

draw.line((235, 140, 265, 140), fill='black')

circle_x = 235
circle_y = 110
circle_radius = 3
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

circle_x = 265
circle_y = 110
circle_radius = 3
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')
img.show()
