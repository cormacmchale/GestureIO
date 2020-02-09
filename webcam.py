import cv2
import keyboard
import keras as kr

# Get model onto server for use
from keras.models import load_model
<<<<<<< HEAD
import keyboard
from matplotlib import pyplot as plt
=======
>>>>>>> e5703c326e2c69113292087cd9c042704e3b9be7
import numpy as np
import PIL
from PIL import Image 
import webbrowser 

numberRecoq = load_model('savedModel/imageRecog.h5')

# Thread issue fix
from returnPrediction import abstractPredic

# Remove black bars from video
webcam = cv2.VideoCapture(cv2.CAP_DSHOW)

running = True

basewidth = 100
firstThreshold = 40
secondThreshold = 60
startLeft = 80
startTop = 80
endRight = 300
endBottom = 300
color = (0, 0, 0)
thickness = 1
frameCounter = 2
captureCounter = 2
captureImages = False

print('Recording...')

while (running):
    check, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 7, 50, 50)
    edges = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    edgesFiltered = cv2.Canny(grayFiltered, firstThreshold, secondThreshold)
    
    cv2.imshow("SignWriter", edges)
    cv2.imshow("filtered", edgesFiltered)

    key = cv2.waitKey(1)


    # Build a large set of images
    if(captureImages):
        cv2.imwrite('temp/originalImage.png', edgesFiltered)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        f = open('dataset/data/imagedata.npy', 'a')
        data = np.asarray(img, dtype='uint8')
        np.savetxt(f, data, fmt='%s')        
        f.close()
        captureCounter = captureCounter + 1
        # Stop appending images
        if(captureCounter==200):
            captureImages = False
            # Reset
            print("finished")
            captureCounter = 0
    
    #analyse every x amount of frames
    frameCounter = frameCounter + 1
    if(frameCounter %  55 == 0):
        cv2.imwrite('temp/originalImage.png', edgesFiltered)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        data = np.asarray(img, dtype='uint8').reshape(1,48400)
        inputVector = data.copy()
        #img = np.array(Image.open(filename))
        #inputVector.setflags(write=1)
        inputVector[inputVector > 0] = 1
        inputVector[inputVector < 1] = 0
        prediction = abstractPredic(data, numberRecoq)
        f = open('predictions/checkPrediction.txt', 'a')
        # Perfrom action here for gesture recognition
        if(prediction == 0):
            f.write("No Gesture" + "\n")
        elif (prediction == 1):
            f.write("Open Hand" + "\n")
            #webbrowser.open('https://learnonline.gmit.ie/', new=2)
            #removed for testing
        elif(prediction == 2):
            f.write("Peace Sign" + "\n")
        elif(prediction == 3):
            f.write("A MIGHTY FIST" + "\n")
        elif(prediction == 4):
            f.write("Garbage" + "\n")
        else:
            f.write("ERROR: You shouldn't see this")
        f.close()
        frameCounter = 0
      
    #user interaction
    # If user presses 'c', begin capture for 100 frames
    if key == ord('c'):
        if(captureImages):
            captureImages = False
        else:
            captureImages = True
    if key == ord('p'):
        cv2.imwrite('temp/originalImage.png', edgesFiltered)
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        data = np.asarray(img, dtype='uint8').reshape(1,48400)
        # data[data > 0] = 1
        # data[data < 1] = 0
        prediction = abstractPredic(data, numberRecoq)
        f = open('predictions/checkPrediction.txt', 'a')
        # Perfrom action here for gesture recognition
        if(prediction == 0):
            f.write("No Gesture" + "\n")
        elif (prediction == 1):
            f.write("Open" + "\n")
            #webbrowser.open('https://www.google.com/', new=2)
        elif(prediction == 2):
            f.write("Peace Sign" + "\n")
            keyboard.write("hello friend")
        else:
            f.write("ERROR: You shouldn't see this")
        f.close()
    if key == ord('q'):
        print('Quitting program...')  
        running = False
        break  

    #organising the edges detection
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