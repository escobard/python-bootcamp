from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 5
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
  # cancels tkinters window timer
  window.after_cancel()
  canvas.itemconfig(timer_text, text="00:00")
  title_label.config(text="Timer")
  checkmark_label.config(text="")
  global reps
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

# calls the countodwn function to begin the timer
def start_timer():
  global reps
  reps += 1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  count_down(work_sec)
  if reps % 8 == 0:
    count_down(long_break_sec)
    title_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    title_label.config(text="Break", fg=PINK)
  else:
    count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import time

def count_down(count):

  # converts seconds to minute / second timer
  ## math.floor(returns largest wholenumber)
  count_min = math.floor(count / 60)

  # returns the number of seconds that remain after being cleanly divided by 60
  ## eg 100 / 60 = 40
  ### eg count = 10 && count % 60 = 40
  count_sec = count % 60

  # handle second count for 0
  if count_sec == 0:
    count_sec = "00"

  # handle second logic for less than 10 seconds
  if count < 10 and count_sec != 0:
    ## on dynamic types with python https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    ### python allows you to change the variable type by adding a different type of value
    count_sec = f"0{count_sec}"

  # change canvas to return new time
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  # prevents counts in the negative
  if count > 0:
    ## makes a local var globally available in a methods
    global timer
    # .after calls a specified function after the specified time
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    mark = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      mark += "✓"
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas with tkinter - allows us to draw an image on the screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

# PhotoImage - function with tkinter to read an image file
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# for color palettes, can try https://colorhunt.co/
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark_label = Label(fg=GREEN, font=(FONT_NAME, 12), bg=YELLOW)
checkmark_label.grid(column=1,row=3)

window.mainloop()