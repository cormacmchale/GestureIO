import tkinter as tk
from tkinter import *
import cv2

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

webcam = cv2.VideoCapture(cv2.CAP_DSHOW)


running = True

while (running):
    check, frame = webcam.read()
    test = Label(window,frame)
    test.grid(row = 4, column = 4)
    window.mainloop()
    #cv2.imshow("filtered", edgesFiltered)
    key = cv2.waitKey(1)

    if key == ord('q'):
        print('Quitting program...')  
        running = False
        break

# Stop the webcam
webcam.release()

cv2.destroyAllWindows

