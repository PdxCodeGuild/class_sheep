from turtle import *
screen = Screen()
screen.bgcolor("black")

bill = Turtle()
bill.shape("turtle")
bill.color("#01cdfe")
bill.pensize(12)
bill.right(72)

jenn = Turtle()
jenn.shape("turtle")
jenn.color("#ff71ce")
jenn.pensize(12)
jenn.right(144)

todd = Turtle()
todd.shape("turtle")
todd.color("#05ffa1")
todd.pensize(12)
todd.right(216)

kate = Turtle()
kate.shape("turtle")
kate.color("#b967ff")
kate.pensize(12)
kate.right(288)

brad = Turtle()
brad.shape("turtle")
brad.color("#fffb96")
brad.pensize(12)
brad.right(0)

n_sides = 3
edge_length = 20
i = 2
while i < 100:
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
    edge_length += 20

done()
