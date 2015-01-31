#!/usr/bin/env python 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cam.set(4, 320)
cam.set(5, 320)
cam.set(6, 320)


while True:
    ret, img = cam.read()

    if ret:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        green_low = np.array([100, 50, 80])
        green_high = np.array([110, 255, 255])

        mask = cv2.inRange(hsv, green_low, green_high)


        res = cv2.bitwise_and(img, img, mask =  mask)

        cv2.imshow("frame", res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
