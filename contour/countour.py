import cv2
import numpy as np

img = cv2.imread('../imgs/teste.png', cv2.IMREAD_GRAYSCALE)

# Threshold the image.
thresholded_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]

mainContours,_ = cv2.findContours(thresholded_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

mainContours = [countor for countor in mainContours if cv2.contourArea(countor)>=10]

countMainContours = len(mainContours)
    
mainContour = max(mainContours, key=cv2.contourArea)

# Encontra o menor retângulo que se inscreve no contorno
rectangle = cv2.minAreaRect(mainContour)

# Calcula a posição e ângulo parcial da camisa com base no retângulo
'''center = rectangle[0]
centerMeters = pixel2meters(self._world, center, component_mask.shape)
angle = rectangle[-1]'''

cv2.drawContours(img, mainContour, contourIdx=-1, color=(0, 255, 0), thickness=5, lineType=cv2.LINE_AA)

# Display the image.
cv2.imshow('Image with contours', img)
cv2.waitKey(0)