from tkinter import *
from random import *
from pandas import *
BACKGROUND_COLOR = "#B1DDC6"
FRENCH = "French"
ENGLISH = "English"
rand_card = {}
rem_words = {}
try:
    word_data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = read_csv("data/french_words.csv")
    rem_words = word_data.to_dict(orient="records")
else:
    rem_words = word_data.to_dict(orient="records")


# ____________________Create New Flash Card______________________________
def gen_random_word():
    global rand_card, flip_timer, word_data
    window.after_cancel(flip_timer)

    data_dict = word_data.to_dict(orient="records")
    rand_card = choice(data_dict)
    canvas.itemconfig(card_title, text=FRENCH, fill="Black")
    canvas.itemconfig(card_word, text=rand_card["French"], fill="Black")
    canvas.itemconfig(cardb_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global rand_card
    canvas.itemconfig(card_title, text=ENGLISH, fill="White")
    canvas.itemconfig(card_word, text=rand_card["English"], fill="White")
    canvas.itemconfig(cardb_img, image=back_img)


def remove_word():
    global rand_card
    word_data.remove(rand_card)
    to_learn = DataFrame(word_data)
    to_learn.to_csv("data/words_to learn.csv")

    gen_random_word()


# ____________________UI Setup______________________________
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
cardb_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, command=gen_random_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right, bg=BACKGROUND_COLOR, command=remove_word)
right_button.grid(row=1, column=1)

gen_random_word()

window.mainloop()
