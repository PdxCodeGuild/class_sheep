from turtle import *
screen = Screen()
screen.bgcolor("black")

bill = Turtle()
bill.shape("turtle")
bill.color("#01cdfe")
bill.pensize(4)

jenn = Turtle()
jenn.shape("turtle")
jenn.color("#ff71ce")
jenn.pensize(4)

todd = Turtle()
todd.shape("turtle")
todd.color("#05ffa1")
todd.pensize(4)

kate = Turtle()
kate.shape("turtle")
kate.color("#b967ff")
kate.pensize(4)

brad = Turtle()
brad.shape("turtle")
brad.color("#fffb96")
brad.pensize(4)

n_sides = 3
edge_length = 20
i = 2
while i < 100:
    for x in range(3):
        bill.left(x*30)
        bill.forward(edge_length)
        jenn.right(x*60)
        jenn.forward(edge_length)
        todd.right(x*90)
        todd.forward(edge_length)
        kate.right(x*120)
        kate.forward(edge_length)
        brad.right(x*150)
        brad.forward(edge_length)

        i = i + 1
    edge_length += 20

done()
