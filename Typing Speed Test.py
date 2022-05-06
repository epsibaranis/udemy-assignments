# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:49:22 2022

@author: tt
"""
from tkinter import *
import re
SECONDS = 10
time = None
timer_time = SECONDS
def timer():
    global time
    global timer_time
    text_area.grid(column=1, row=1)
    if timer_time != 0:
        timer_time -= 1
        start_label["text"] = str(timer_time)
        time = window.after(1000, timer)
    else:
        word_per_second()
def word_per_second():
    text_words = len(text_area.get('1.0', 'end').split())
    word_per_second = round(text_words / SECONDS, 2)
    start_label["text"] = 'Words Per Second: '+str(word_per_second)
window = Tk()
window.title("Type Speed Test")
window.config(padx=50, pady=50)

start_label = Label(text="Let's Start?", font=(
    "Courier", 24, "bold"))
start_label.grid(column=1, row=0)

button_start = Button(text="Yes", font=(
    "Courier", 24, "bold"), padx=100, command=timer)
button_start.grid(column=1, row=2)


text_area = Text(window, height=8)

window.mainloop()

