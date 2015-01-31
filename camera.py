#!/usr/bin/env python 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

cam = cv2.VideoCapture(1)

cam.set(4, 320)
cam.set(5, 320)


while True:
    ret, img = cam.read()

    if ret:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        green_low = np.array([80, 90, 80])
        green_high = np.array([120, 255, 255])

        mask = cv2.inRange(hsv, green_low, green_high)

        res = cv2.bitwise_and(img, img, mask = mask)
        gres = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        sift = cv2.FeatureDetector_create("STAR")
        kp = sift.detect(gres, None)
        if kp:
            xd = [float(k.pt[0]) for k in kp]
            yd = [float(k.pt[1]) for k in kp]

            # sort the data
            reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
            xd = [xd[ii] for ii in reorder]
            yd = [yd[ii] for ii in reorder]

            par = np.polyfit(xd, yd, 1, full=True)
            intercept=int(par[0][1])
            slope=int(640*par[0][0] + intercept)
            cv2.line(img, (0,intercept), (640, slope), (0,0, 255), 5)

        cv2.imshow("frame", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
