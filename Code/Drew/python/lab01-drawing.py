from turtle import *
screen = Screen()
screen.bgcolor("black")

bill = Turtle()
bill.color("#01cdfe")
bill.pensize(3)
bill.right(72)

jenn = Turtle()
jenn.color("#ff71ce")
jenn.pensize(3)
jenn.right(144)

todd = Turtle()
todd.color("#05ffa1")
todd.pensize(3)
todd.right(216)

kate = Turtle()
kate.color("#b967ff")
kate.pensize(3)
kate.right(288)

brad = Turtle()
brad.color("#fffb96")
brad.pensize(3)
brad.right(0)

n_sides = 3
edge_length = 10
i = 2
while i < 50000:
    for x in range(3):
        bill.right(x*144)
        bill.forward(edge_length)
        jenn.right(x*144)
        jenn.forward(edge_length)
        todd.right(x*144)
        todd.forward(edge_length)
        kate.right(x*144)
        kate.forward(edge_length)
        brad.right(x*144)
        brad.forward(edge_length)

        i = i + 1
    edge_length += x

done()
