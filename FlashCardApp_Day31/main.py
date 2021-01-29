from tkinter import *
import pandas as pd
import random

root = Tk()
root.title("Chinese-English Flash Cards")
root.configure(bg="#B1DDC6", padx=50, pady=50)

# ---------------------------- Fetch data and generate random word ------------------------------- #

random_word = {}

try:
    with open("data/words_to_learn.csv") as file:
        unknown_words = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
        words_to_learn = unknown_words
except FileNotFoundError:
    data = pd.read_csv("data/zh-en.csv").to_dict(orient="records")
    words_to_learn = data

def generate_random_card():
    global random_word
    random_word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language, text='Chinese')
    canvas.itemconfig(word, text=random_word['Chinese'])
    canvas.itemconfig(language, fill='black')
    canvas.itemconfig(word, fill='black')
    wrong_btn['state'] = 'disabled'
    right_btn['state'] = 'disabled'
    root.after(3000, flip_card)


def remove_card():
    # print(random_word)
    # print(len(words_to_learn))
    words_to_learn.remove(random_word)
    new_words_df = pd.DataFrame(words_to_learn)
    new_words_df.to_csv('data/words_to_learn.csv', index=False)
    # print(len(words_to_learn))
    generate_random_card()




# ---------------------------- UI SETUP ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language, fill='white')
    canvas.itemconfig(word, fill='white')
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(word, text=random_word['English'])
    wrong_btn['state'] = 'normal'
    right_btn['state'] = 'normal'


root.after(3000, flip_card)
# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, bd=0, command=generate_random_card)
wrong_btn.grid(column=0, row=1)

right_btn_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_image, highlightthickness=0, bd=0, command=remove_card)
right_btn.grid(column=1, row=1)

generate_random_card()

root.mainloop()
