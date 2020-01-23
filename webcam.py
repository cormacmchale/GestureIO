import cv2, time
import numpy as np
import keyboard
from matplotlib import pyplot as plt
from PIL import Image  
import PIL

# Remove black bars from video
webcam = cv2.VideoCapture(cv2.CAP_DSHOW)
running = True
while (running):
    check, frame = webcam.read()
    # Use Canny to find edges in the image
    newFrame = cv2.rectangle(frame, (80,80), (300, 300), (0, 255, 0), 1) 
    edges = cv2.Canny(frame, 100, 100)
    #edgesTwo = frame[80:80,300:300]

    cv2.imshow("Capturing...", edges)
    

    # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # cv2.waitKey(0)

    # Wait for user input
    key = cv2.waitKey(1)

    # If user presses 'Q', program will will quit
    if key == ord('q'):
        cv2.imwrite('check.jpg',cv2.Canny(frame, 100, 100))
        basewidth = 100
        img = Image.open('check.jpg')
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('resize.jpg') 
        #edgesCheck = newEdges.thumbnail(100,Image.ANTIALIAS)
        #cv2.imshow(edgesCheck)
        running = False
        # Save numpy array to text file
        # np.savetxt("imagedata.txt", edges.reshape((3, -1)), fmt="%s", header=str(frame.shape)) # With header
        pixelinfo = cv2.imread('resize.jpg')
        print(pixelinfo.size)
        np.savetxt("imagedata.txt", pixelinfo.reshape((3,-1))) # Without header
        break

# Stop the webcam
webcam.release()

cv2.destroyAllWindows