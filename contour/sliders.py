import cv2
import numpy as np  

def callback(x):
    pass

#cap = cv2.VideoCapture(0)
#cap = cv2.imread("../imgs/defaulthomogra.png")
cap = cv2.imread("../imgs/teste.png")


cv2.namedWindow('image')

ilowG = 0
ihighG = 255

ilowH = 0
ihighH = 255
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change

cv2.createTrackbar('lowH','image',ilowH,255,callback)
cv2.createTrackbar('highH','image',ihighH,255,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)


while True:
    # grab the frame
    
    #img_gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    #ret, frame = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    #ret, frame = cap.read()
    ret, frameG = cv2.threshold(cap, 150, 255, cv2.THRESH_BINARY)
    
    #cv2.imshow('thresholdgray',frameG)
    
    # get trackbar positions
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')
 
    hsv = cv2.cvtColor(frameG, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    cv2.imshow('MASK', mask)
    frame = cv2.bitwise_and(frameG, frameG, mask=mask)
    cv2.imshow('frame', frame)
    
    
    
    
    concatenadas = np.concatenate((cap, frame), axis=1)
    cv2.imshow('image', concatenadas)

    k = cv2.waitKey(1000) & 0xFF # large wait time to remove freezing
    if k == 113 or k == 27:
        break