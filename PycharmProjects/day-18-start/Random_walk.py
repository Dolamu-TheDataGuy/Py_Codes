import turtle as t
import random as ran
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")


for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(ran.choice(directions))