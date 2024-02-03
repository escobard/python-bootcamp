from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
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
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky=EW)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()