#lab16
#imagemanipulation
from PIL import Image
import colorsys
img = Image.open("rainbow.jpg")
width, height = img.size
pixels = img.load()
greyscale = input("Type Yes to render this image in greyscale. >")
if greyscale.lower() == 'yes':
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i,j]
            y = (0.299 * r) + (0.587 * g) + (0.114 * b)
            r = int(round(y))
            g = int(round(y))
            b = int(round(y))
            pixels[i, j] = (r, g, b)
hue_adjust = float(input("Type hue adjustment from -1.0 to 1.0. >"))
sat_adjust = float(input("Type saturation adjustment from -1.0 to 1.0. >"))
val_adjut = float(input("Type value adjustment from -1.0 to 1.0. >"))
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i,j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h = h + hue_adjust
        s = s + sat_adjust
        v = v + val_adjut
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pixels[i, j] = (r, g, b)
img.show()
