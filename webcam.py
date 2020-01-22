import cv2, time
import numpy as np

webcam = cv2.VideoCapture(0)

a = 0

while True:
    check, frame = webcam.read()

    print(check)
    print(frame)

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing...", grayscale)

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