#!/usr/bin/env python 
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import numpy as np
import sklearn
import json
import time

ms = open("masterswing.json", "r")
mswing = json.loads(ms.read())
mcenter_x = [line[0] for line in mswing["centers"]]
mcenter_y = [line[1] for line in mswing["centers"]]

s = open("swing.json", "r")
swing = json.loads(s.read())
scenter_x = [line[0] for line in swing["centers"]]
scenter_y = [line[1] for line in swing["centers"]]


#for i in range(len(swing["centers"])):
#    if swing["lines"][i][0]:
#        cv2.line(img, (0, swing["lines"][i][0]), (640, swing["lines"][i][1]), (0, 255, 0), 3)
#    if swing["centers"][i][0]:
#        cv2.circle(img, (swing["centers"][i][0], swing["centers"][i][1]), 50, (0,0, 255))
for i in range(min(len(scenter_y), len(mcenter_y))):
    if scenter_x[i] and scenter_y[i]:
        if mcenter_x[i] and mcenter_y[i]:
            plt.scatter(scenter_x[i], 500-scenter_y[i], [i,i,i], 0.75)
            plt.scatter(mcenter_x[i], 500-mcenter_y[i], [i,i,i])
plt.show()
