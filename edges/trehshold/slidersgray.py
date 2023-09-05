import cv2
import numpy as np

def threshold_image(img, thresh, maxThresh):
  thresholded_img = cv2.threshold(img, thresh, maxThresh, cv2.THRESH_BINARY)[1]
  return thresholded_img

img = cv2.imread('../imgs/defaulthomogra.png', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('../imgs/teste.png', cv2.IMREAD_GRAYSCALE)

# Create a window to display the image.
cv2.namedWindow('image')

# Create a trackbar to control the threshold value.
cv2.createTrackbar('minThreshold', 'image', 0, 255, threshold_image)
cv2.createTrackbar('maxThreshold', 'image', 0, 255, threshold_image)


while True:
  # Get the current threshold value.
  minThreshold = cv2.getTrackbarPos('minThreshold', 'image')
  maxThreshold = cv2.getTrackbarPos('maxThreshold', 'image')

  # Threshold the imag
  print(minThreshold,maxThreshold)
  thresholded_img = threshold_image(img, minThreshold, maxThreshold)

  # Display the thresholded image.
  cv2.imshow('image', thresholded_img)

  # Check if the user wants to quit.
  k = cv2.waitKey(1) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()