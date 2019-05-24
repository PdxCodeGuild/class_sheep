#Lab 16 - Image Manipulation
#version 1 - convert image to greyscale

from PIL import Image
img = Image.open("C:\\Users\\Lane\\Documents\\Bootcamp\\python_projects\\in_progress\\rainbow.jpg") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        average = int(0.299*r) + int(0.587*g) + int(0.114*b)
        pixels[i, j] = (average, average, average)
        # (255-r, 255-g, 255-b)

img.show()
