from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

class Password:

  def __init__(self):
    self.website: str = ""
    self.email: str = ""
    self.password: str = ""

  def update_values(self):
    self.update_website()
    self.update_email()
    self.update_password()
    self.update_file()

  def update_website(self):
    website_value: str = website_entry.get()
    self.website = website_value
    # delete entry value
    ## https://tkdocs.com/tutorial/widgets.html#entry
    website_entry.delete(0, "end")

  def update_email(self):
    email_value: str = email_entry.get()
    self.email = email_value
    email_entry.delete(0, "end")

  def update_password(self):
    password_value: str = password_entry.get()
    self.password = password_value
    password_entry.delete(0, "end")

  def update_file(self):
    ## https://www.w3schools.com/python/python_file_write.asp
    password_file = open("passwords.txt", "a")
    ## adding \n to create new line after each entry
    ### https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
    password_file.write(f"{self.website} / {self.email} / {self.password}\n")
    password_file.close()


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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky=EW)
add_button = Button(text="Add", width=36, command=password_store.update_values)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
