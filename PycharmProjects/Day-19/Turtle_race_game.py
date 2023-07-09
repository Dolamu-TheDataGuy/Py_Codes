# Code to build a turtle race game
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_delta = 0
for c in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[c])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + y_delta)
    all_turtle.append(new_turtle)
    y_delta += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
