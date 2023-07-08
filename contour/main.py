import numpy as np  
import cv2

img = cv2.imread('../imgs/gwen.jpg')  
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary image', thresh)
#cv2.imshow('ret', ret)
cv2.waitKey(0)

#cv2.imshow('imgs2',img)
'''

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)  
ret, thresh = cv.threshold(imgray, 127, 255, 0)  
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  '''