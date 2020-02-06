import cv2
import keyboard
import keras as kr

# Get model onto server for use
from keras.models import load_model
from matplotlib import pyplot as plt
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
firstThreshold = 100
secondThreshold = 100
startLeft = 80
startTop = 80
endRight = 300
endBottom = 300
color = (0, 255, 0)
thickness = 1
frameCounter = 0
captureCounter = 0
captureImages = False

print('Recording...')

while (running):
    check, frame = webcam.read()
    # cv2.rectangle() method is used to draw a rectangle on any image - gesture will be performed within the 
    # rectangle - For proccessing the image, the dataset will be built from the image captured within the rectangle
    newFrame = cv2.rectangle(frame, (startLeft - 5, startTop - 5), (endRight + 5, endBottom + 5), color, thickness)
    # Use Canny to find edges in the image
    edges = cv2.Canny(frame, firstThreshold, secondThreshold)
    # edgesTwo = frame[80:80,300:300]
    cv2.imshow("SignWriter", edges)
    key = cv2.waitKey(1)


    # Build a large set of images
    if(captureImages):
        cv2.imwrite('temp/originalImage.png', cv2.Canny(frame, 100, 200))
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
            captureCounter = 0
    
    #analyse every x amount of frames
    captureCounter = captureCounter + 1
    if(captureCounter % 60 == 0):
        cv2.imwrite('temp/originalImage.png', cv2.Canny(frame, 100, 100))
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
            webbrowser.open('https://www.google.com/', new=2)
        elif(prediction == 2):
            f.write("Peace Sign" + "\n")
        else:
            f.write("ERROR: You shouldn't see this")
        f.close()
        captureCounter = 0
      
    #user interaction
    # If user presses 'c', begin capture for 100 frames
    if key == ord('c'):
        if(captureImages):
            captureImages = False
        else:
            captureImages = True
    if key == ord('p'):
        cv2.imwrite('temp/originalImage.png', cv2.Canny(frame, 100, 100))
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
            webbrowser.open('https://www.google.com/', new=2)
        elif(prediction == 2):
            f.write("Peace Sign" + "\n")
        else:
            f.write("ERROR: You shouldn't see this")
        f.close()
    if key == ord('q'):
        print('Quitting program...')  
        running = False
        break  

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