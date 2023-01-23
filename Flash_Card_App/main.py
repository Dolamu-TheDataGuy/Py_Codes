from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
word_to_learn = data.to_dict(orient='records') # A list of dictionaries
print(word_to_learn)


def next_card():
    current_card=random.choice(word_to_learn)


window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure the window

# Canvas
canvas = Canvas(width=800, height=526)  # Image overlaid on window
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 90, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 250, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)
window.mainloop()
