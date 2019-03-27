#lab1.py
'''Turtle'''

from turtle import *
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(100)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
left(36)
forward(200)
edge_length = 0
i = 0
while i < 20:
    forward(edge_length)
    right(144)
    edge_length += 4
    i = i + 1
forward(20)
right(90)
forward(13)
right(90)
forward(80)
left(90)
forward(100)
right(45)
forward(100)
right(180)
forward(100)
right(90)
forward(100)

done()
