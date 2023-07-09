import turtle as t
import random as r
tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]


def draw_shape(num_sides):
    for i in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(r.choice(colors))
    draw_shape(shape_side)
