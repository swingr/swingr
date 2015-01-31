#!/usr/bin/env python 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
import json

cam = cv2.VideoCapture(1)

cam.set(10, -1)

frames = []
swing = {"centers" : []}
raw_input("press enter to start recording")
for i in range(200):
#while True:
    _, img = cam.read()
    frames.append(img)

for img in frames:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    xavg, yavg = None, None

    green_low = np.array([50, 90, 100])
    green_high = np.array([100, 255, 255])
    green_mask = cv2.inRange(hsv, green_low, green_high)

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
        cv2.circle(green_res, (xavg, yavg), 50, (0,0, 255))

    swing["centers"].append((xavg, yavg))
    cv2.imshow("frame", green_res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print json.dumps(swing)
f = open("swing.json", "w")
f.write(json.dumps(swing))
cam.release()
cv2.destroyAllWindows()
