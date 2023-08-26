import cv2
import numpy as np

img = cv2.imread("../imgs/teste.png")

# convert to HSV, since red and yellow are the lowest hue colors and come before green
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create a binary thresholded image on hue between red and yellow
lower = (0,0,20)
upper = (1,255,240)
thresh = cv2.inRange(hsv, lower, upper)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# get external contours
contours = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

result1 = img.copy()
result2 = img.copy()
for c in contours:
    cv2.drawContours(result1,[c],0,(0, 255, 0),2)
    # get rotated rectangle from contour
    rot_rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rot_rect)
    box = np.intp(box)
    # draw rotated rectangle on copy of img
    cv2.drawContours(result2,[box],0,(0, 255, 0),2)

# save result
cv2.imwrite("./resultsball/4cubes_thresh.jpg",thresh)
cv2.imwrite("./resultsball/4cubes_clean.jpg",clean)
cv2.imwrite("./resultsball/4cubes_result1.png",result1)
cv2.imwrite("./resultsball/4cubes_result2.png",result2)

# display result
cv2.imshow("thresh", thresh)
cv2.imshow("clean", clean)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()