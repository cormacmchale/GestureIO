import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

path = 'gestureImages/openhand.png'

window = tk.Tk()

window.title("SignWriter")
window.geometry("700x500")
window.configure(bg="white")

photo = PhotoImage(file=path)

w = Label(window, image=photo)

w.grid(row=3, column=3)

window.mainloop()