import cv2
import numpy as np

img = cv2.imread('/content/drive/MyDrive/UnBall/Treinamentos/Colab Notebooks/imgs/defaulthomogra.png')

retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)  
cv2.imshow("Original Image", img)  
cv2.imshow("Threshold",threshold)  
cv2.waitKey(0)  