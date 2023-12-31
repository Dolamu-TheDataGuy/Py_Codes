import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state_list = data['state'].to_list()

guessed_state = []


while len(guessed_state) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in all_state_list if state not in guessed_state]
        # for state in all_state_list:
            # if state not in guessed_state:
                # states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


def get_mouse_click_coord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coord)

turtle.mainloop()

screen.exitonclick()
