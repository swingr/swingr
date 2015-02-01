#!/usr/bin/env python 
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from math import sqrt
import numpy as np
import sklearn
import json
import time
import requests

s = open("swing.json", "r")
swing = json.loads(s.read())
scenter_x = [line[0] for line in swing["centers"]]
scenter_y = [line[1] for line in swing["centers"]]

totals = []
for i in range(10):
    ms = open("masters/masterswing%d.json" % (i+1), "r")
    mswing = json.loads(ms.read())
    mcenter_x = [line[0] for line in mswing["centers"]]
    mcenter_y = [line[1] for line in mswing["centers"]]

    dists = []
    x = []
    y = []
    x1 = []
    y1 = []
    x2, x3 = [], []
    y2, y3 = [], []
    for i in range(min(len(scenter_y), len(mcenter_y))):
        if mcenter_x[i] and mcenter_y[i]:
            if mcenter_y[i] > 250:
                y1.append(mcenter_y[i])
                x1.append(mcenter_x[i])
            if mcenter_y[i] < 250:
                y3.append(mcenter_y[i])
                x3.append(mcenter_x[i])
        if scenter_x[i] and scenter_y[i]:
            if scenter_y[i] > 250:
                x.append(scenter_x[i])
                y.append(scenter_y[i])
            if scenter_y[i] < 250:
                x2.append(scenter_x[i])
                y2.append(scenter_y[i])
    d= -1
    z = np.polyfit(np.array(x[:d]), np.array(y[:d]), 2)
    f = np.poly1d(z)
    x_new = np.linspace(x[:d][0], x[:d][-1], 100)
    y_new = f(x_new)

    z1 = np.polyfit(np.array(x1[:d]), np.array(y1[:d]), 2)
    f = np.poly1d(z1)
    x_new = np.linspace(x1[:d][0], x1[:d][-1], 100)
    y_new = f(x_new)


    z2 = np.polyfit(np.array(x2[:d]), np.array(y2[:d]), 2)
    f = np.poly1d(z2)
    x_new = np.linspace(x2[:d][0], x2[:d][-1], 100)
    y_new = f(x_new)

    z3 = np.polyfit(np.array(x3[:d]), np.array(y3[:d]), 2)
    f = np.poly1d(z3)
    x_new = np.linspace(x3[:d][0], x3[:d][-1], 100)
    y_new = f(x_new)

    total = abs(z[0]-z1[0]) + abs(z[1]-z1[1]) + abs(z[2]-z1[2])+ abs(z2[0]-z3[0])+\
        abs(z2[1]-z3[1])+ abs(z2[2]-z3[2])
    totals.append(max((200-total)/2, 0))
avg = np.mean(totals)
ip = "http://138.51.202.24:5000"
r = requests.get(ip + "/score/" + str(avg))
if avg < 20:
    requests.get(ip + "/existence")
elif avg < 40:
    requests.get(ip + "/frustrating")
elif avg < 60:
    requests.get(ip + "/choke")
elif avg < 80:
    requests.get(ip + "/shoulders")
else:
    requests.get(ip + "/frustrating")
print("done")
