from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)

window.mainloop()