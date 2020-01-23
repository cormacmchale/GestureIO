import cv2, time
import numpy as np
import keyboard
from matplotlib import pyplot as plt
from PIL import Image  
import PIL

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
counter = 1
while (running):
    check, frame = webcam.read()
    # Use Canny to find edges in the image
    newFrame = cv2.rectangle(frame, (startLeft, startTop), (endRight, endBottom), color, thickness)
    edges = cv2.Canny(frame, firstThreshold, secondThreshold)
    # edgesTwo = frame[80:80,300:300]
    cv2.imshow("Capturing...", edges)
    key = cv2.waitKey(1)

    # If user presses 'Q', program will will quit
    if key == ord('q'):
        cv2.imwrite(str(counter)+'originalImage.png', cv2.Canny(frame, 100, 100))
        # Open the captured gesture
        img = Image.open(str(counter)+'originalImage.png')
        img = img.crop((startLeft, startTop, endRight, endBottom))
        img.save(str(counter)+'croppedImage.png')
        img.load()
        data = np.asarray(img, dtype="int32" )
        print(data.size)
        #running = False
        np.savetxt(str(counter)+'imagedata.txt', data,fmt='%1.0f')
        counter=counter+1        
        # Save numpy array to text file
        # np.savetxt("imagedata.txt", edges.reshape((3, -1)), fmt="%s", header=str(frame.shape)) # With header

        #pixelInfo = cv2.imread('croppedImage.png')
        # print(pixelinfo.size)

        #pixelInfo[pixelInfo>0] = 255
        #pixelInfo[pixelInfo==0] = 0
                # Unused as for now - revisit when building the dataset
        # wPercent = (basewidth / float(img.size[0]))
        # hSize = int((float(img.size[1]) * float(wPercent)))

        # img = img.resize((basewidth, hSize), Image.ANTIALIAS)
        # img.save('resize.png') 

        # edgesCheck = newEdges.thumbnail(100,Image.ANTIALIAS)
        # cv2.imshow(edgesCheck)

        #np.savetxt("imagedata.txt", data.reshape((3, -1)),fmt='%5.0f') # Without header

        # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        # plt.show()
        # cv2.waitKey(0)
        # Wait for user input

# Stop the webcam
webcam.release()

cv2.destroyAllWindows