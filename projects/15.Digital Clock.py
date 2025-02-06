from tkinter import *
import time

window = Tk()

window.title("Digital Clock")
window.geometry("420x150")
window.resizable(2,1)

label = Label(window,font=("Boulder",68,"bold"),bg="yellow",bd=25,fg="#363529")

label.grid(row=0,column=1)

def clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(400,clock)

clock()
window.mainloop()