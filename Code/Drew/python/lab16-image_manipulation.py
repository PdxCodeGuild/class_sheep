from PIL import Image, ImageDraw

""" This breaks up each pixel of an image and sorts left to right by RGB value """
#import image
img = Image.open("rainbow.jpg") # must be in same folder
width, height = img.size
pixels = img.load()

#get colors
colors = []
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        colors.append((r, g, b))

#sort and draw colors
colors.sort()
img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)
c = 0
for i in range(width):
    for j in range(height):
        draw.point((i, j), fill=colors[c])
        c += 1

img.show()
