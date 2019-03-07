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

# version 2, weird-ass rainbow
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
