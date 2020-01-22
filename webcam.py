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
    edges = cv2.Canny(frame, 100, 100)

    cv2.imshow("Capturing...", edges)

    # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # cv2.waitKey(0)

    # Wait for user input
    key = cv2.waitKey(1)

    # If user presses 'Q', program will will quit
    if key == ord('q'):
        running = False

        # Save numpy array to text file
        # np.savetxt("imagedata.txt", edges.reshape((3, -1)), fmt="%s", header=str(frame.shape)) # With header
        np.savetxt("imagedata.txt", edges.reshape((3, -1)), fmt="%s") # Without header
        break

# Stop the webcam
webcam.release()

cv2.destroyAllWindows