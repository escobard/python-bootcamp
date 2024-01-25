# build a graphical user interface (GUI) for users to interact with
## will leverage the tkinter library, which is natively available with python
### https://docs.python.org/3/library/tkinter.
#### tkinter was built with tk (another language), python is a wrapper around that, which is why this library uses * and ** type of arguments so freely
import tkinter

# to import all modules from a library, we can use:
## from tkinter import *
def button_clicked():
  my_label["text"] = input.get()

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label - not clear what this is
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))

# apply label to the screen
## .pack() places the tkinter object in a relative position on the screen (left, right, center, etc)
### .pack() utilizes the packer, which tkinters geometry-management mechanism
#### https://docs.python.org/3.12/library/tkinter.html#the-packer
#my_label.pack()

# .place() allows us to place/render the element on an x/y axis
## x/y axis center is at the top left corner of the screen!
### the tradeoff with .place() is that it is difficult to find the exact coordinates to place elements
## my_label.place(x=0, y=0)

# .grid() allows us to create a grid and place elements within the grid coordinates
## if using grid positioning, it is best practice to use grid placement for all elements on the screen
### cannot mixup grid and pack, but can use grid and place together
my_label.grid(column=0, row=0)


# can change configuration of objects in numerous ways after creation - https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
## eg - my_label["text"] = "New Text" - updates the text accordingly

# Button

## to manage events (like a click), event handlers need to be developed


## command= sets the callback function in case of an event with the element
button = tkinter.Button(text="Click Me", command=button_clicked)
## .pack must be run to place/render every element on the screen
#button.pack()

button.grid(column=1, row=1)

new_button = tkinter.Button(text='New button')
new_button.grid(column=2, row=0)

# Entry - similar to an HTML input
input = tkinter.Entry(width=10)
#input.pack()
input.grid(column=3, row=2)

## returns the value of the input as a string
## input_value = input.get()

## keeps a window on the screen with tkinter
window.mainloop()