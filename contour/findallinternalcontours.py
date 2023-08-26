import cv2
import numpy as np

img = cv2.imread("../imgs/teste.png")

# convert to HSV, since red and yellow are the lowest hue colors and come before green
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create a binary thresholded image on hue between red and yellow
lower = (0,0,1)
upper = (255,255,255)
thresh = cv2.inRange(hsv, lower, upper)

#ball
lowerBall = (0,0,0)
upperBall = (5,255,245)
threshBall = cv2.inRange(hsv, lowerBall, upperBall)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

kernelBall = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
cleanBall = cv2.morphologyEx(threshBall, cv2.MORPH_OPEN, kernel)
kernelBall = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
cleanBall = cv2.morphologyEx(threshBall, cv2.MORPH_CLOSE, kernel)

# get external contours
contours = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

contoursBall = cv2.findContours(cleanBall, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoursBall = contoursBall[0] if len(contoursBall) == 2 else contoursBall[1]

result1 = img.copy()
result2 = img.copy()

result1Ball = img.copy()
result2Ball = img.copy()

for c in contours:
    cv2.drawContours(result1,[c],0,(0, 255, 0),2)
    # get rotated rectangle from contour
    rot_rect = cv2.minAreaRect(c)
    #print(rot_rect)
    box = cv2.boxPoints(rot_rect)
    box = np.intp(box)
    # draw rotated rectangle on copy of img
    cv2.drawContours(result2,[box],0,(0, 255, 0),2)
    
for c in contoursBall:
    cv2.drawContours(result1Ball,[c],0,(0, 255, 0),2)
    # get rotated rectangle from contour
    rot_rectBall = cv2.minAreaRect(c)
    boxball = cv2.boxPoints(rot_rectBall)
    boxball = np.intp(boxball)
    # draw rotated rectangle on copy of img
    cv2.drawContours(result2Ball,[boxball],0,(0, 255, 0),2)

# save result
cv2.imwrite("./resultsend/4cubes_thresh.jpg",thresh)
cv2.imwrite("./resultsend/4cubes_clean.jpg",clean)
cv2.imwrite("./resultsend/4cubes_result1.png",result1)
cv2.imwrite("./resultsend/4cubes_result2.png",result2)

# display result

#cv2.imshow("thresh", thresh)
#cv2.imshow("clean", clean)
#cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

#cv2.imshow("result1Ball1", result1Ball)
cv2.imshow("result1Ball2", result2Ball)

fgMaskNoBall = cv2.bitwise_and(thresh, cv2.bitwise_not(threshBall))
cv2.imshow("fgMaskNoBall", fgMaskNoBall)

areas = []

for i in range(len(contours)):
    print(contours[i])
    areas.append(cv2.contourArea((np.array(contours[i]))))

print(areas)

for c in contours:
    cv2.drawContours(fgMaskNoBall,[c],0,(0, 255, 0),2)
    rot_rectinternalcontours = cv2.minAreaRect(c)
    boxball = cv2.boxPoints(rot_rectBall)
    boxball = np.intp(boxball)
    
    # draw rotated rectangle on copy of img
    cv2.drawContours(result2Ball,[boxball],0,(0, 255, 0),2)

cv2.waitKey(0)
cv2.destroyAllWindows()