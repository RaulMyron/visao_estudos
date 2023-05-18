   
import cv2  
import numpy as np  
  
img = cv2.imread('imgs/defaultFrame.png')
img_com_homofrafia = cv2.imread('imgs/defaulthomogra.png')
   
cv2.imshow('Original', img) 
cv2.waitKey(0)
cv2.imshow('Pos homografia', img_com_homofrafia) 
cv2.waitKey(0)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
hsv_homography = cv2.cvtColor(img_com_homofrafia, cv2.COLOR_BGR2HSV)

cv2.imshow('Original HSV', hsv) 
cv2.waitKey(0)
cv2.imshow('Pos homografia HSV', hsv_homography)  
cv2.waitKey(0)

lower_red = np.array([30, 150, 50])  
upper_red = np.array([255, 255, 180])  
 
mask = cv2.inRange(hsv, lower_red, upper_red)  
mask_homography = cv2.inRange(hsv_homography, lower_red, upper_red)  

cv2.imshow('Mask ORIGINAL HSV', mask)
cv2.waitKey(0)
cv2.imshow('Mask post homography HSV', mask_homography)
cv2.waitKey(0)

# discovers edges in the input image image and   
# marks them in the output map edges 

edges = cv2.Canny(img, 100, 200) 
edges_homography = cv2.Canny(img_com_homofrafia, 100, 200) 
#não tirei as linhas brancas, com o slider é mto mais fácil

# Display edges in a frame   
cv2.imshow('Edges', edges)  
cv2.waitKey(0)
cv2.imshow('Edges', edges_homography) 
cv2.waitKey(0)

cv2.destroyAllWindows() 