# build a graphical user interface (GUI) for users to interact with
## will leverage the tkinter library, which is natively available with python
### https://docs.python.org/3/library/tkinter.
#### tkinter was built with tk (another language), python is a wrapper around that, which is why this library uses * and ** type of arguments so freely
import tkinter

# to import all modules from a library, we can use:
## from tkinter import *

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label - not clear what this is
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))

# apply label to the screen
## .pack() centers the tkinter object on the screen
### .pack() utilizes the packer, which tkinters geometry-management mechanism
#### https://docs.python.org/3.12/library/tkinter.html#the-packer
my_label.pack()


# can change configuration of objects in numerous ways after creation - https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
## eg - my_label["text"] = "New Text" - updates the text accordingly

# Button

## to manage events (like a click), event handlers need to be developed
def button_clicked():
  my_label["text"] = input.get()

## command= sets the callback function in case of an event with the element
button = tkinter.Button(text="Click Me", command=button_clicked)
## .pack must be run to place/render every element on the screen
button.pack()

# Entry - similar to an HTML input
input = tkinter.Entry(width=10)
input.pack()

## returns the value of the input as a string
## input_value = input.get()

## keeps a window on the screen with tkinter
window.mainloop()