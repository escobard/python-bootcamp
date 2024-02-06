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
    self.words_file = ""
    self.random_choice = ""
    self.words_dictionary: list[dict] = [self.word_list]
    self.words_to_learn: list[dict] = [self.word_list]
    self.flip_timer = window.after(3000, func=self.flip_card)
    self.load_words()

  def load_words(self):
    try:
      self.words_file = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
      self.words_file = pandas.read_csv("./data/french_words.csv")
    finally:
      self.words_dictionary = self.words_file.to_dict(orient="records")
      self.words_to_learn = self.words_file.to_dict(orient="records")

      self.random_choice = random.choices(self.words_dictionary)
      self.word_list = self.random_choice[0]
      self.word = self.word_list[self.language]

      print(self.words_dictionary)
  def next_card(self):
    self.pick_word()
    self.store_words_to_learn()

  def skip_card(self):
    self.pick_word()

  def store_words_to_learn(self):
    # remove found words from known list of words
    self.words_to_learn.remove(self.word_list)

    # STEP 4
    # 1. When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word should be removed from the list of words that might come up.
    # 2. The updated data should be saved to a new file called words_to_learn.csv
    # 3. The next time the program is run, it should check if there is a words_to_learn.csv file. If it exists, the program should use those words to put on the flashcards. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it should use the words in the french_words.csv. We want our flashcard program to only test us on things we don't know. So if the user presses the ✅ button, that means the current card should not come up again.

    # store known list of words to file
    words_to_learn_file = pandas.DataFrame(self.words_to_learn)
    words_to_learn_file.to_csv("./data/words_to_learn.csv")


  def pick_word(self):
    ## invalidates old timer to reset delay
    window.after_cancel(self.flip_timer)

    # picks new word in French
    self.language = "French"
    self.random_choice = random.choices(self.words_dictionary)
    self.word_list = self.random_choice[0]
    self.word = self.word_list[self.language]
    print(self.word_list)

    # update gui with new data
    canvas.itemconfig(language_text, text=self.language, fill="black")
    canvas.itemconfig(word_text, text=self.word, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)

    ## creates new timer to re-start time delay
    self.flip_timer = window.after(3000, func=self.flip_card)

  # STEP 3
  # 1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
  #
  # 2. The card image should change to the card_back.png and the text colour should change to white. The title of the card should change to "English" from "French".
  def flip_card(self):
    self.language = "English"
    self.word = self.word_list[self.language]

    canvas.itemconfig(language_text, text=self.language, fill="white")
    canvas.itemconfig(word_text, text=self.word, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


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
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flashcards_store = Flashcards()
# canvas text
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text=flashcards_store.language, fill="black")
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text=flashcards_store.word, fill="black")

# columnspan is required to ensure flashcard object takes two columns' worth of space, otherwise buttons become misaligned
canvas.grid(row=0, column=0, columnspan=2)


# image buttons

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=flashcards_store.next_card)

known_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                        command=flashcards_store.skip_card)
unknown_button.grid(row=1, column=0)

window.mainloop()