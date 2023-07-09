import turtle as t
import random as ran
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
