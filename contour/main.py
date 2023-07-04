import numpy as np  
import cv2

im = cv2.imread('../imgs/camisa0.png')  
#img = cv2.imread('imgs/defaultFrame.png')

cv2.imshow('img1',im)
cv2.waitKey()
#cv2.imshow('imgs2',img)
'''
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)  
ret, thresh = cv.threshold(imgray, 127, 255, 0)  
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  '''