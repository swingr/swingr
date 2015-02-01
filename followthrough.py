#!/usr/bin/env python 
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import numpy as np
import sklearn
import json
import time

s = open("swing.json", "r")
swing = json.loads(s.read())
scenter_x = [line[0] for line in swing["centers"]]
scenter_y = [line[1] for line in swing["centers"]]

q1 = q2 = q3 = q4 = 0

plots = []
m1 = m2 = 0

for i in range(min(len(scenter_x), len(scenter_y))):
	if scenter_y[i] and scenter_x[i]:
		#top left
		if scenter_x[i] < 250 and scenter_y[i] < 250:
			q1 += 1
		#top right
		elif scenter_x[i] > 250 and scenter_y[i] < 250:
			q2 += 1
		#bottom left
		elif scenter_x[i] < 250 and scenter_y[i] > 250:
			q3 += 1
		#bottom right
		elif scenter_x[i] > 250 and scenter_y[i] > 250:
			q4 += 1


buffer = 15
flag = 0

average = (q1 + q2 + q3 + q4)/4
print q1
print q2
print q3
print q4

if abs(q1 - average) < 10:
	flag += 1	
if abs(q2 - average) < 10:
	flag += 1
if abs(q3 - average) < 10:
	flag += 1
if abs(q4 - average) < 10:
	flag += 1

if flag >= 3:
	print "Great"
else:
	print "meh"





