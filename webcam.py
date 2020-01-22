import cv2, time
import numpy as np
import keyboard
from matplotlib import pyplot as plt

webcam = cv2.VideoCapture(0)

a = 0

while True:
    check, frame = webcam.read()
    cv2.imshow("Capturing...", frame)
    edges = cv2.Canny(frame,100,100)
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    # cv2.waitKey(0)
    key = cv2.waitKey(1)
    if key == ord('q'):
        running = False
        # Save numpy array to text file
        np.savetxt("test.txt", frame.reshape((3,-1)), fmt="%s", header=str(frame.shape))
        # numpy.save("nxx.npy", frame)
        break
webcam.release()
cv2.destroyAllWindows