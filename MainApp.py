# Imports for pre-processing and application building
import cv2
import keras as kr
from keras.models import load_model
import numpy as np
import PIL
from PIL import Image, ImageTk 
from returnPrediction import abstractPredic
import tkinter as tk
from tkinter import Label, Entry, PhotoImage, StringVar

# Imports for user actions
import os
import webbrowser

# Variables
startLeft, startTop = 80, 80
endRight, endBottom = 300, 300
color = (0, 0, 0)
thickness = 1
firstThreshold = 50
secondThreshold = 50
numberRecoq = load_model('savedModel/imageRecog.h5')

webcam = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)

# Building the GUI
webcam = cv2.VideoCapture(cv2.CAP_DSHOW)

root = tk.Tk()
root.title("Gesture IO")
# root.configure(bg="black")

openhand = './frontend/gestureImages/openhand.png'
fist = './frontend/gestureImages/fist.png'
peacesign = './frontend/gestureImages/peacesign.png'
thumbandpinky = './frontend/gestureImages/thumbandpinky.png'

photoOne = PhotoImage(file=openhand)
photoTwo = PhotoImage(file=fist)
photoThree = PhotoImage(file=peacesign)
photoFour = PhotoImage(file=thumbandpinky)

OpenHandCommand = StringVar()
FistCommand = StringVar()
showUser = StringVar()
urltext = StringVar()

urltext.set("Enter URL to get in browser")
programtext = StringVar()
programtext.set("Enter desktop app name to launch")
peacetext = StringVar()
peacetext.set("TBC...")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

frame1 = tk.Frame(root)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, padx=10)

w1 = tk.Label(frame2, image=photoOne).grid(row=0, column=0, sticky="nsew")
e1 = tk.Entry(frame2, textvariable=OpenHandCommand).grid(row=0, column=1)
s1 = tk.Label(frame2, textvariable=urltext).grid(row=0, column=1, pady=(0,40))

w2 = Label(frame2, image=photoTwo).grid(row=1, column=0, pady=50, sticky="nsew")
e2 = tk.Entry(frame2, textvariable=FistCommand).grid(row=1, column=1)
s2 = Label(frame2, textvariable=programtext).grid(row=1, column=1, pady=(0,40))

w3 = Label(frame2, image=photoThree).grid(row=2, column=0, sticky="nsew")
e3 = tk.Entry(frame2).grid(row=2, column=1)
s3 = Label(frame2, textvariable=peacetext).grid(row=2, column=1,pady=(0,40))
# s3.place(side="top")

w4 = Label(frame1, textvariable=showUser).grid(row=1, column=0)
main = tk.Label(frame1)
main.grid(row=0, column=0)

# Tracking frames for intermittent prediction 
frameCounter = 0

def showWebcam():
    # Grab frame data from web-cam
    _, frame = webcam.read()

    # Pre-processing of the frame data
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 7, 25, 25)
    grayFilteredAgain = cv2.GaussianBlur(grayFiltered, (3, 3), 0)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    edgesFiltered = cv2.Canny(grayFilteredAgain, firstThreshold, secondThreshold)
    fgmask = fgbg.apply(edgesFiltered)
    # End pre-processing

    # Generate web-cam capture for user display within the GUI
    cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2Image)
    imgTK = ImageTk.PhotoImage(image=img)
    main.imTK = imgTK
    main.configure(image=imgTK)
    main.after(5, showWebcam)
    # End GUI  web-cam display

    # Measure Frames Processed
    global frameCounter
    frameCounter = frameCounter + 1

    if(frameCounter %  60 == 0):
        # Begin pre-processing/formatting for neural network
        cv2.imwrite('temp/originalImage.png', fgmask)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        data = np.asarray(img, dtype='uint8').reshape(1, 48400)

        inputVector = data.copy()
        inputVector[inputVector > 0] = 1
        inputVector[inputVector < 1] = 0

        prediction = abstractPredic(inputVector, numberRecoq)
        # End preprocessing

        # Begin user gesture take action
        if(prediction == 0):
            url = OpenHandCommand.get()

            if (url== ""):
                showUser.set("Open Hand")   
            else:
                showUser.set("Open Hand")
                webbrowser.open(url, new=2)
        elif (prediction == 1):
            showUser.set("Peace Sign")
        elif(prediction == 2):
            shellcmd = FistCommand.get()

            if(shellcmd==""):
                showUser.set("Fist")
            else:
                showUser.set("Fist")
                os.startfile("C://Users//Cormac//Desktop//"+shellcmd)
        elif(prediction == 3):
            showUser.set("Ignore Gesture")
        # End user gesture take action

        frameCounter = 0

# Call show web-cam to begin capturing frames
showWebcam()

# Begin looping GUI for display
root.mainloop()