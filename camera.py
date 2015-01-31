#!/usr/bin/env python 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

cam = cv2.VideoCapture(1)

cam.set(10, 0)

frames = []
raw_input("press enter to start recording")
while True:
#for i in range(300):
    _, img = cam.read()
 #   frames.append(img)

#for img in frames:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    blue_low = np.array([50, 0, 0])
    blue_high = np.array([170, 100, 20])
    blue_mask = cv2.inRange(img, blue_low, blue_high)

    blue_res = cv2.bitwise_and(img, img, mask = blue_mask)
    gres = cv2.cvtColor(blue_res, cv2.COLOR_BGR2GRAY)

    feature = cv2.SURF()
    kp = feature.detect(gres, None)
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
        cv2.line(img, (0,intercept), (640, slope), (0,0, 255), 3)
        #res = cv2.drawKeypoints(blue_res, kp, (0, 255, 0))
#        _, cnts, _ = cv2.findContours(gres, cv2.RETR_LIST,
#                cv2.CHAIN_APPROX_TC89_KCOS)
#        max_cnt = None
#        max_cnt_area = 0
#        for cnt in cnts:
#            area = cv2.contourArea(cnt)
#            if area > max_cnt_area:
#                max_cnt = cnt
#        cv2.drawContours(res, [max_cnt], -1, (0, 0, 255, 2))
    green_low = np.array([80, 120, 80])
    green_high = np.array([100, 200, 100])
    green_mask = cv2.inRange(img, green_low, green_high)

    green_res = cv2.bitwise_and(img, img, mask = green_mask)
    gres = cv2.cvtColor(green_res, cv2.COLOR_BGR2GRAY)

    feature = cv2.ORB()
    kp = feature.detect(gres, None)
    if kp:
        xd = [float(k.pt[0]) for k in kp]
        yd = [float(k.pt[1]) for k in kp]

        # sort the data
        reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
        xd = [xd[ii] for ii in reorder]
        yd = [yd[ii] for ii in reorder]

        xavg = int(reduce(lambda x, y: x + y, xd) / len(xd))
        yavg = int(reduce(lambda x, y: x + y, yd) / len(yd))
        cv2.circle(img, (xavg, yavg), 50, (0,0, 255))

    cv2.imshow("frame", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
