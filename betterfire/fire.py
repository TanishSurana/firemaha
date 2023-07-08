import cv2
import numpy as np
import time

path = 'GH017626.MP4'
cap = cv2.VideoCapture(path)
suc, prev = cap.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)


while True:

    suc, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # start time to calculate FPS
    # start = time.time()

    # # End time
    # end = time.time()
    # # calculate the FPS for current frame detection
    # fps = 1 / (end-start)

    # print(f"{fps:.2f} FPS")

    cv2.imshow('flow', prevgray)


    key = cv2.waitKey(5)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()