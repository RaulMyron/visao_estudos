import cv2
 
img = cv2.imread('imgs/lobo_guara.jpg') 

cv2.imshow('Original', img)
cv2.waitKey(0)

#detectamos melhor no cinza e melhor com o fundo desfocado
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_cinza, (3,3), 0) 
 
# Sobel detecção de bordas
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel para o eixo X
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel para o eixo Y
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Sobel para XY comutativos

cv2.imshow('Sobel X', sobelx)
cv2.imwrite('outputs/sobel/x.jpg', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.imwrite('outputs/sobel/y.jpg', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.imwrite('outputs/sobel/xy.jpg', sobelxy)
cv2.waitKey(0)
 
cv2.destroyAllWindows()