from turtle import Turtle, Screen

# import turtle as tr
# from turtle import * Not a good way of importing modules

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)


screen = Screen()
screen.exitonclick()

# have to download module
import heroes
print(heroes.gen())
