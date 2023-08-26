import cv2
import numpy as np
 
img = cv2.imread("../imgs/card.jpeg")
 
# Pontos selecionados
red_point = [516,136]
green_point = [938,296]
blue_point = [692,854]
black_point = [308,696]
 
# Ciando uma matriz de pontos
matrix_de_pontos = np.float32([red_point,green_point,black_point, blue_point])
 
# Draw circle for each point
cv2.circle(img,(red_point[0],red_point[1]),10,(0,0,255),cv2.FILLED)
cv2.circle(img,(green_point[0],green_point[1]),10,(0,255,0),cv2.FILLED)
cv2.circle(img,(blue_point[0],blue_point[1]),10,(255,0,0),cv2.FILLED)
cv2.circle(img,(black_point[0],black_point[1]),10,(0,0,0),cv2.FILLED)
 
# Output image size
largura, altura = 250,350
 
# Desired points value in output images
converted_red_pixel_value = [0,0]
converted_green_pixel_value = [largura,0]
converted_blue_pixel_value = [largura,altura]
converted_black_pixel_value = [0,altura]
 
# Nova matriz de conversao
matrix_convertida = np.float32([converted_red_pixel_value,converted_green_pixel_value,
                               converted_black_pixel_value,converted_blue_pixel_value])
 
# perspective transform
transformacao = cv2.getPerspectiveTransform(matrix_de_pontos,matrix_convertida)

img_saida = cv2.warpPerspective(img,transformacao,(largura,altura))
 
cv2.imshow("img_entrada", img)
cv2.imshow("img_saida", img_saida)
cv2.waitKey(0)