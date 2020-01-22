import cv2, time

webcam = cv2.VideoCapture(0)

a = 0
running = True

while (running):
    a += 1

    check, frame = webcam.read()

    print(check)
    print(frame)

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing...", grayscale)

    # cv2.waitKey(0)
    key = cv2.waitKey(1)

    if key == ord('q'):
        running = False
        break

print(a)

webcam.release()

cv2.destroyAllWindows