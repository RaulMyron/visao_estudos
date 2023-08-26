import cv2
import numpy as np

def get_contour(img, thresh, method):
  # Threshold the image.
  thresholded_img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

  # Find the contours.
  contours, _ = cv2.findContours(thresholded_img, cv2.RETR_TREE, method)

  # Return the contours.
  return contours

img = cv2.imread('../imgs/teste.png', cv2.IMREAD_GRAYSCALE)

# Create a window to display the image.
cv2.namedWindow('Image with contours')

# Create trackbars to control the threshold value and the contour approximation method.
cv2.createTrackbar('Threshold', 'Image with contours', 0, 255, get_contour)
cv2.createTrackbar('Method', 'Image with contours', 0, 3, get_contour)

while True:
  # Get the current threshold value and the contour approximation method.
  thresh = cv2.getTrackbarPos('Threshold', 'Image with contours')
  method = cv2.getTrackbarPos('Method', 'Image with contours')

  # Get the contours.
  contours = get_contour(img, thresh, method)

  # Draw the contours.
  cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

  # Display the image.
  cv2.imshow('Image with contours', img)

  # Check if the user wants to quit.
  k = cv2.waitKey(1) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()