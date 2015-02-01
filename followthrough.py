#!/usr/bin/env python 
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import numpy as np
import sklearn
import json
import time

def followthrough():
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

	total = q1 + q2 + q3 + q4
	buffer = 0.1 * total
	deviant = int((q1 + q2 + q3 + q4)*buffer)

	aq1 = 0.24
	aq2 = 0.35
	aq3 = 0.19
	aq4 = 0.06

	if (q2 < ((total * aq2) - buffer)) or (q2 > ((total * aq2) + buffer)):
		return False
	if (q4 < ((total * aq4) - buffer)) or (q4 > ((total * aq4) + buffer)):
		return False
	else:
		return True



