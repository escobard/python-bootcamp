from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #

## chose to build solution with a class to practice OOP, could have been simpler to keep it as pure functions
class Password:

  def __init__(self):
    self.website: str = ""
    self.email: str = ""
    self.password: str = ""
    self.errors: bool = False
    self.json_data = {}

  def update_values(self):
    self.website = website_entry.get()
    self.email = email_entry.get()
    self.password = password_entry.get()
    self.validate_entries()

    if not self.errors:
      # returns boolean with user answer
        self.clear_fields()
        self.update_file()

  def clear_fields(self):
    # delete entry value
    ## https://tkdocs.com/tutorial/widgets.html#entry
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")
    self.json_data = {}
    # commenting delete for now, until favorite email is fetched from file
    # email_entry.delete(0, "end")

  def update_file(self):
    self.json_data = {
      self.website: {
        "email": self.email,
        "password": self.password
      }
    }
    ## use python's JSON module to manage json data - https://docs.python.org/3/library/json.html
    ## first read data from file
    try:
      with open("data.json", "r") as password_file:
        print("File was found")
    except FileNotFoundError:
      print("File was not found")
      ## replace existing data in file with updated data
      print("Creating file")
      with open("data.json", "w") as password_file:
        # dumps json data back into the file
        json.dump(self.json_data, password_file, indent=4)
    else:
      with open("data.json", "r") as password_file:
        print("Loading file's data")
        data = json.load(password_file)
        # updates json data with new json data
        data.update(self.json_data)
      with open("data.json", "w") as password_file:
        print("Updating file with", self.json_data)
        json.dump(data, password_file, indent=4)


  def load_json(self):
    password_file = open("data.json", "r")
    data = json.load(password_file)
    ## converts json data to python dictionary
    print(type(data))
    password_file.close()

  def validate_entries(self):
    if len(self.website) == 0 or len(self.email) == 0 or len(self.password) == 0:
      self.errors = True
      messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
      self.errors = False

  # ---------------------------- PASSWORD GENERATOR ------------------------------- #

  def generate_password(self):

    ## from password generator project on day/section 5!

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # remove forloops by using list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers;

    shuffle(password_list)

    # appends all characters from a list to a string
    password = "".join(password_list)
    self.password = password
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")

# ---------------------------- UI SETUP ------------------------------- #

password_store = Password()

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white")
## grid sticky property places elements to the left of the grid cell instead of the center
website_label.grid(row=1, column=0, sticky=EW)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky=EW)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky=EW)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
## focus allows the user to begin typing into the entry on program startup
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
## insert places a value within an entry
### first argument the text within the specified x axis coordinates
email_entry.insert(0, "dan@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_store.generate_password)
generate_password_button.grid(row=3, column=2, sticky=EW)
add_button = Button(text="Add", width=36, command=password_store.update_values)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
