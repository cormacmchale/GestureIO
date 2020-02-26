import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

w, h = 800, 600
webcam = cv2.VideoCapture(0)

openhand = 'gestureImages/openhand.png'
fist = 'gestureImages/fist.png'

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, w)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

root = tk.Tk()
root.title("SignWriter")
root.geometry("900x700")
root.configure(bg="white")
root.bind('<Escape>', lambda e: root.quit())

photoOne = PhotoImage(file=openhand)
photoTwo = PhotoImage(file=fist)

w1 = Label(root, image=photoOne)
w2 = Label(root, image=photoTwo)

w1.grid(row=3, column=3)
w2.grid(row=3, column=2)

main = tk.Label(root)
main.grid(row=1, column=1)

def showWebcam():
    _, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2Image)
    imgTK = ImageTk.PhotoImage(image=img)

    main.imTK = imgTK
    main.configure(image=imgTK)
    main.after(5, showWebcam)

showWebcam()
root.mainloop()
