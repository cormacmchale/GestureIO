import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

# Variables
width, height = 450, 450
startLeft, startTop = 80, 80
endRight, endBottom = 300, 300
color = (0, 0, 0)
thickness = 1

webcam = cv2.VideoCapture(0)

openhand = 'gestureImages/openhand.png'
fist = 'gestureImages/fist.png'

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.title("SignWriter")
root.geometry("900x700")
root.configure(bg="white")
root.bind('<Escape>', lambda e: root.quit())

photoOne = PhotoImage(file=openhand)
photoTwo = PhotoImage(file=fist)

w1 = Label(root, image=photoOne)
e1 = tk.Entry(root)

w2 = Label(root, image=photoTwo)
e2 = tk.Entry(root)

w1.grid(row=0, column=2)
e1.grid(row=0, column=3)
w2.grid(row=1, column=2)
e2.grid(row=1, column=3)

main = tk.Label(root)
main.grid(row=1, column=1)

def showWebcam():
    _, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    
    cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2Image)
    imgTK = ImageTk.PhotoImage(image=img)

    main.imTK = imgTK
    main.configure(image=imgTK)
    main.after(5, showWebcam)

showWebcam()
root.mainloop()
