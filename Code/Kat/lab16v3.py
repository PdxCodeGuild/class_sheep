from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


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
