#!/usr/bin/env python 
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from math import sqrt
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

dists = []
for i in range(min(len(scenter_y), len(mcenter_y))):
    if mcenter_x[i] and mcenter_y[i]:
        if scenter_x[i] and scenter_y[i]:
            dists.append(sqrt((scenter_y[i] - mcenter_y[i]) ** 2 + (scenter_y[i]
                - mcenter_y[i]) ** 2))
print 1 - (np.mean(dists)/max(dists))

plt.show()
