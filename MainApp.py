import tkinter as tk
from tkinter import *
import cv2

import keras as kr
from keras.models import load_model
import numpy as np

import PIL
from PIL import Image, ImageTk 
import webbrowser
from returnPrediction import abstractPredic

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)
numberRecoq = load_model('savedModel/imageRecog.h5')

# Variables
width, height = 450, 450
startLeft, startTop = 80, 80
endRight, endBottom = 300, 300
color = (0, 0, 0)
thickness = 1
firstThreshold = 50
secondThreshold = 50

webcam = cv2.VideoCapture(0)

openhand = './frontend/gestureImages/openhand.png'
fist = './frontend/gestureImages/fist.png'
peacesign = './frontend/gestureImages/peacesign.png'
thumbandpinky = './frontend/gestureImages/thumbandpinky.png'

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
showUser = StringVar()

# def assignGesture():
#     print("Empty")

w1 = Label(root, image=photoOne).grid(row=0, column=2)
e1 = tk.Entry(root, textvariable=test).grid(row=0, column=3)
# btn = Button(root, text="Assign Command", command=assignGesture).grid(row=0, column=4)

w2 = Label(root, image=photoTwo).grid(row=1, column=2)
e2 = tk.Entry(root).grid(row=1, column=3)

w3 = Label(root, image=photoThree).grid(row=2, column=2)
e3 = tk.Entry(root).grid(row=2, column=3)

w4 = Label(root, textvariable=showUser).grid(row=2, column=1)
# e4 = tk.Entry(root).grid(row=4, column=3)

# Possible choices for dropdown menu (possibly implemented later?)
gestureChoices = ["Open Browser", "Open Word", "Open Command Line Prompt"]

main = tk.Label(root)
main.grid(row=1, column=1)
stringVar = tk.StringVar(root)
stringVar.set(gestureChoices[0])
dropdownMenu = OptionMenu(root, stringVar, *gestureChoices)
# dropdownMenu.grid(row=2, column=2)
#global frameCounter
frameCounter = 0
def showWebcam():
    _, frame = webcam.read()
    #frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 7, 25, 25)
    grayFilteredagain = cv2.GaussianBlur(grayFiltered, (3, 3), 0)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    edgesFiltered = cv2.Canny(grayFilteredagain, firstThreshold, secondThreshold)
    fgmask = fgbg.apply(edgesFiltered)
    #cv2.imshow("SignWriter", fgmask)
    cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2Image)
    imgTK = ImageTk.PhotoImage(image=img)
    main.imTK = imgTK
    main.configure(image=imgTK)
    main.after(5, showWebcam)
    #analyse every x amount of frames
    global frameCounter
    frameCounter = frameCounter + 1
    if(frameCounter %  60 == 0):
        cv2.imwrite('temp/originalImage.png', fgmask)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        #NewImg = img.save("temp/croppedPrediction.png");
        data = np.asarray(img, dtype='uint8').reshape(1, 48400)
        inputVector = data.copy()
        inputVector[inputVector > 0] = 1
        inputVector[inputVector < 1] = 0
        prediction = abstractPredic(inputVector, numberRecoq)
        if(prediction == 0):
            url = test.get()
            if (url== ""):
                #w4.config(text="Open Hand")
                showUser.set("Open Hand")   
            else:
                showUser.set("Open Hand")
                webbrowser.open(url, new=2)
        elif (prediction == 1):
            showUser.set("Peace Sign") 
        elif(prediction == 2):
            showUser.set("Fist") 
            #subprocess.call(['C:\Program Files\Microsoft VS Code\Code.exe'])
        elif(prediction == 3):
            showUser.set("Ignore Gesture") 
        frameCounter = 0
        f.close()
showWebcam()
#print(test)
root.mainloop()
