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
peacesign = 'gestureImages/peacesign.png'
thumbandpinky = 'gestureImages/thumbandpinky.png'

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.title("SignWriter")
root.geometry("1000x1000")
root.configure(bg="white")
root.bind('<Escape>', lambda e: root.quit())

photoOne = PhotoImage(file=openhand)
photoTwo = PhotoImage(file=fist)
photoThree = PhotoImage(file=peacesign)
photoFour = PhotoImage(file=thumbandpinky)

test = StringVar()

# def assignGesture():
#     print("Empty")

w1 = Label(root, image=photoOne).grid(row=0, column=2)
e1 = tk.Entry(root, textvariable=test).grid(row=0, column=3)
# btn = Button(root, text="Assign Command", command=assignGesture).grid(row=0, column=4)

w2 = Label(root, image=photoTwo).grid(row=1, column=2)
e2 = tk.Entry(root).grid(row=1, column=3)

w3 = Label(root, image=photoThree).grid(row=2, column=2)
e3 = tk.Entry(root).grid(row=2, column=3)

# w4 = Label(root, image=photoFour).grid(row=3, column=2)
# e4 = tk.Entry(root).grid(row=4, column=3)

# Possible choices for dropdown menu (possibly implemented later?)
gestureChoices = ["Open Browser", "Open Word", "Open Command Line Prompt"]

main = tk.Label(root)
main.grid(row=1, column=1)


stringVar = tk.StringVar(root)
stringVar.set(gestureChoices[0])

dropdownMenu = OptionMenu(root, stringVar, *gestureChoices)
# dropdownMenu.grid(row=2, column=2)

def showWebcam():
    _, frame = webcam.read()
    #frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2Image)
    imgTK = ImageTk.PhotoImage(image=img)
    main.imTK = imgTK
    main.configure(image=imgTK)
    main.after(5, showWebcam)

showWebcam()
print(test)
root.mainloop()
