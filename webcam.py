import cv2
import keyboard
from matplotlib import pyplot as plt
import numpy as np
import PIL
from PIL import Image  

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

print('Recording...')

while (running):
    check, frame = webcam.read()

    # cv2.rectangle() method is used to draw a rectangle on any image - gesture will be performed within the 
    # rectangle - For proccessing the image, the dataset will be built from the image captured within the rectangle
    newFrame = cv2.rectangle(frame, (startLeft-5, startTop-5), (endRight+5, endBottom+5), color, thickness)

    # Use Canny to find edges in the image
    edges = cv2.Canny(frame, firstThreshold, secondThreshold)
    # edgesTwo = frame[80:80,300:300]

    cv2.imshow("SignWriter", edges)
    key = cv2.waitKey(1)

    # If user presses 'Q', program will capture image
    if key == ord('c'):
        # Save frame of webcam to an image
        cv2.imwrite('temp/originalImage.png', cv2.Canny(frame, 120, 120))

        # Open the captured gesture
        # No need to create multiple original images as the dataset won't be built from this image
        img = Image.open('temp/originalImage.png') 
        img = img.crop((startLeft, startTop, endRight, endBottom))
        
        #img.save('dataset/images/croppedImage.png')
        #img.load()

        data = np.asarray(img, dtype='int32')
        data[data>0] = 1
        print(data.shape)
        f = open('dataset/data/imagedata.txt','a')
        np.savetxt(f, data, fmt='%s', delimiter='')
        f.close();

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