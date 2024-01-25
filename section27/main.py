# build a graphical user interface (GUI) for users to interact with
## will leverage the tkinter library, which is natively available with python
### https://docs.python.org/3/library/tkinter.
#### tkinter was built with tk (another language), python is a wrapper around that, which is why this library uses * and ** type of arguments so freely
import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label - not clear what this is
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))

# apply label to the screen
## .pack() centers the tkinter object on the screen
### .pack() utilizes the packer, which tkinters geometry-management mechanism
#### https://docs.python.org/3.12/library/tkinter.html#the-packer
my_label.pack(side='left')


## keeps a window on the screen with tkinter
window.mainloop()