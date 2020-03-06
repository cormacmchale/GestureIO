import cv2
import keyboard
import keras as kr
from matplotlib import pyplot as plt

# Get model onto server for use
from keras.models import load_model
import numpy as np
import PIL
from PIL import Image 
import webbrowser
import subprocess

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)
numberRecoq = load_model('../savedModel/imageRecog.h5')

# Thread issue fix
from returnPrediction import abstractPredic

# Remove black bars from video
webcam = cv2.VideoCapture(cv2.CAP_DSHOW)

running = True

basewidth = 100
firstThreshold = 50
secondThreshold = 50
startLeft = 80
startTop = 80
endRight = 300
endBottom = 300
color = (0, 0, 0)
thickness = 1
frameCounter = 2
captureCounter = 0
captureImages = False

print('Recording...')

while (running):
    check, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 7, 25, 25)
    grayFilteredagain = cv2.GaussianBlur(grayFiltered, (3, 3), 0)
    frame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    edgesFiltered = cv2.Canny(grayFilteredagain, firstThreshold, secondThreshold)
    
    fgmask = fgbg.apply(edgesFiltered)

    #cv2.imshow('frame',fgmask)
    cv2.imshow("SignWriter", frame)
    
    #cv2.imshow("filtered", edgesFiltered)
    key = cv2.waitKey(1)

    # Build a large set of images
    if(captureImages):
        cv2.imwrite('temp/originalImage.png', fgmask)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        f = open('dataset/data/imagedata.npy', 'a')
        data = np.asarray(img, dtype='uint8')
        np.savetxt(f, data, fmt='%s')        
        f.close()

        captureCounter = captureCounter + 1
        # Stop appending images
        if(captureCounter==300):
            captureImages = False

            # Reset
            print("finished")
            running = False
            captureCounter = 0
    
    #analyse every x amount of frames
    frameCounter = frameCounter + 1

    if(frameCounter %  30 == 0):
        cv2.imwrite('temp/originalImage.png', fgmask)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        data = np.asarray(img, dtype='uint8').reshape(1, 48400)
        inputVector = data.copy()

        # img = np.array(Image.open(filename))
        # inputVector.setflags(write=1)

        inputVector[inputVector > 0] = 1
        inputVector[inputVector < 1] = 0
        prediction = abstractPredic(inputVector, numberRecoq)
        
        f = open('predictions/checkPrediction.txt', 'a')
        # Perfrom action here for gesture recognition
        if(prediction == 0):
            f.write("Open Hand" + "\n")
        elif (prediction == 1):
            f.write("Peace Sign" + "\n")
            #url = name.get()
            url = ""
            if (url== ""):
                #do nothing
                print("Empty")
            else:
                webbrowser.open(url, new=2)

            #removed for testing
        elif(prediction == 2):
            f.write("A MIGHTY FIST" + "\n")
            #subprocess.call(['C:\Program Files\Microsoft VS Code\Code.exe'])
        elif(prediction == 3):
            f.write("Ignore Gesture" + "\n")
        else:
            f.write("ERROR: You shouldn't see this")

        f.close()
        frameCounter = 0
      
    # User interaction
    # If user presses 'c', begin capture for 100 frames
    if key == ord('c'):
        if(captureImages):
            captureImages = False
        else:
            captureImages = True

    #practice foreground
    #https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html
    if key == ord('p'):
        cv2.imwrite('temp/originalImage.png', frame)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        img.save('temp/croppedImage.png')    
        ##have the image here
        #imgTwo = cv2.imread('temp/croppedImage.png')
        #mask = np.zeros(imgTwo.shape[:2],np.uint8) 
        #bgdModel = np.zeros((1,65),np.float64)
        #fgdModel = np.zeros((1,65),np.float64)
        #rect = (0, 0, 200, 200)
        #cv2.grabCut(imgTwo,mask,rect,bgdModel,fgdModel,2,cv2.GC_INIT_WITH_RECT)
        #mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        #imgTwo = imgTwo*mask2[:,:,np.newaxis]
        #plt.imshow(imgTwo),plt.colorbar(),plt.show()
    if key == ord('q'):
        print('Quitting program...')  
        running = False
        break
    # Organising the edge detection manually
    if key == ord('y'):
        firstThreshold = firstThreshold + 20
        print ("first Threshold "+str(firstThreshold))
    if key == ord('h'):
        firstThreshold = firstThreshold - 20  
    if key == ord('u'):
        secondThreshold = secondThreshold + 20
        print ("second Threshold "+str(secondThreshold))
    if key == ord('j'):
        secondThreshold = secondThreshold - 20 

# Stop the webcam
webcam.release()

cv2.destroyAllWindows

''' Unused code '''
''' =========== '''
# Save numpy array to text file
        # np.savetxt("imagedata.txt", edges.reshape((3, -1)), fmt="%s", header=str(frame.shape)) # With header

        # pixelInfo = cv2.imread('croppedImage.png')
        # print(pixelinfo.size)

        # pixelInfo[pixelInfo>0] = 255
        # pixelInfo[pixelInfo==0] = 0

        # Unused as for now - revisit when building the dataset
        # wPercent = (basewidth / float(img.size[0]))
        # hSize = int((float(img.size[1]) * float(wPercent)))

        # img = img.resize((basewidth, hSize), Image.ANTIALIAS)
        # img.save('resize.png') 

        # edgesCheck = newEdges.thumbnail(100,Image.ANTIALIAS)
        # cv2.imshow(edgesCheck)

        # np.savetxt("imagedata.txt", data.reshape((3, -1)),fmt='%5.0f') # Without header

        # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        # plt.show()

        # Wait for user input
        # cv2.waitKey(0)