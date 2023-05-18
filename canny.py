import cv2

img = cv2.imread('imgs/lobo_guara.jpg') 

cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

edges = cv2.Canny(img_blur, 50, 100) 
edges1 = cv2.Canny(img_blur, 100, 100) 
edges2 = cv2.Canny(img_blur, 100, 200) 
edges3 = cv2.Canny(img_blur, 100, 150) 
edges4 = cv2.Canny(img_blur, 180, 200) 

cv2.imshow('Canny Edge 0', edges)
cv2.waitKey(0)
cv2.imshow('Canny Edge 1', edges1)
cv2.waitKey(0)
cv2.imshow('Canny Edge 2', edges2)
cv2.waitKey(0)
cv2.imshow('Canny Edge 3', edges3)
cv2.waitKey(0)
cv2.imshow('Canny Edge 4', edges4)
cv2.waitKey(0)

cv2.imwrite('outputs/canny/canny_output1.jpg', edges)
cv2.imwrite('outputs/canny/canny_output2.jpg', edges1)
cv2.imwrite('outputs/canny/canny_output2.jpg', edges2)
cv2.imwrite('outputs/canny/canny_output3.jpg', edges3)
cv2.imwrite('outputs/canny/canny_output4.jpg', edges4)

cv2.destroyAllWindows()
 