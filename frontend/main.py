import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

openhand = 'gestureImages/openhand.png'
fist = 'gestureImages/fist.png'

window = tk.Tk()

window.title("SignWriter")
window.geometry("700x500")
window.configure(bg="white")

# toolbar = Frame(window, bg="blue")
# toolbar.pack(side=TOP, fill=X)

photoOne = PhotoImage(file=openhand)
photoTwo = PhotoImage(file=fist)

w1 = Label(window, image=photoOne)
w2 = Label(window, image=photoTwo)

w1.grid(row=3, column=3)
w2.grid(row=3, column=2)

window.mainloop()