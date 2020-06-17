# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:46:09 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = plt.imread(r"D:\OpenCV\opencv-master\samples\data\board.jpg",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = np.uint8(img)
print(img.shape)
cv2.imshow('Image',img)
img1 = cv2.Canny(img,120,250)
cv2.imshow('Edge_Detection',img1)
cv2.waitKey(50000)
cv2.destroyAllWindows()