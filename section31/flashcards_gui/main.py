# STEP 2
# 1. Read the data from the french_words.csv file in the data folder.
#
# 2. Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display. e.g.
import pandas
import random


class Flashcards:

  def __init__(self):
    self.language: str = "French"
    self.word: str = "trouve"
    self.word_list: dict = {"French": "perdu", "English": "lost"}
    self.words_dictionary: list[dict] = [{}]
    self.load_words()

  def load_words(self):
    words_file = pandas.read_csv("./data/french_words.csv")
    # creates each column in a {row:value} format
    self.words_dictionary = words_file.to_dict(orient="records")
    print(self.words_dictionary)

  def next_card(self):
    self.language = "French"
    canvas.itemconfig(language_text, text=self.language)
    random_choice = random.choices(self.words_dictionary)
    self.word_list = random_choice[0]
    self.word = self.word_list[self.language]
    canvas.itemconfig(word_text, text=self.word)

  # STEP 3
  # 1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
  #
  # 2. The card image should change to the card_back.png and the text colour should change to white. The title of the card should change to "English" from "French".
  def reveal_answer(self):
    window.after(3000, self.reveal_answer())
    self.language = "English"
    canvas.itemconfig(language_text, text=self.language)
    self.word = self.word_list[self.language]
    canvas.itemconfig(word_text, text=self.word)


# STEP 1
# 1. Download the starting files from the course resources.
# 2. Use the images in the image folder, to create the user interface. The ❌ and ✅ are buttons. You can add images to buttons like this:
#
# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)
#
# 3. Here are some hints for the fonts, measurements and positioning.
# HINTS:
#
# 1. You will need a 2 X 2 grid, with the flash card taking up 2 columns.
#
# 2. The flash card is a Canvas with 1 image and 2 pieces of text.
#
# 3. The image is card_front.png, created from the PhotoImage class. Be careful about the full image path as the image is inside the image folder.

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# card image
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas text
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title", fill="black")
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="Word", fill="black")

# columnspan is required to ensure flashcard object takes two columns' worth of space, otherwise buttons become misaligned
canvas.grid(row=0, column=0, columnspan=2)
flashcards_store = Flashcards()

# image buttons

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=flashcards_store.next_card)

known_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                        command=flashcards_store.reveal_answer)
unknown_button.grid(row=1, column=0)

window.mainloop()