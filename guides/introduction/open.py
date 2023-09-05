import cv2
import numpy as np
#from google.colab.patches import cv2_imshow

img = cv2.imread("../imgs/pogcat.png")
cv2.imshow("gato", img)

pixel = img[100,100]
altura = img.shape[0]
largura = img.shape[1]
tamanho = img.size

print('pixel', pixel)
print('altura', altura)
print('largura', largura)
print('tamanho kb', tamanho)

nova_largura = 350
nova_altura = 450
novas_dimensoes = (nova_largura, nova_altura)

#resize 

img_formatada = cv2.resize(img, novas_dimensoes, interpolation=cv2.INTER_AREA)

pixel = img[100,100]
altura = img.shape[0]
largura = img.shape[1]
tamanho = img.size

print('pixel', pixel)
print('altura', altura)
print('largura', largura)
print('tamanho em kb', tamanho)

pixel_img_formatada = img_formatada[100,100]
altura_img_formatada = img_formatada.shape[0]
largura_img_formatada = img_formatada.shape[1]
tamanho_img_formatada = img_formatada.size

print('Novas propriedades : ')
print('pixel', pixel)
print('altura', altura_img_formatada)
print('largura', largura_img_formatada)
print('tamanho em kb', tamanho_img_formatada)

cv2.imshow("oi", img_formatada) # --> rodando no colab

#rotacao 

(altura, largura) = img_formatada.shape[:2]
centro = (altura / 2, largura / 2)

escala = 1.0 #Mantém igual
#90º (coordenada central, ângulo de rotação, escala)
M = cv2.getRotationMatrix2D(centro, 90, escala)

rotaçao_90 = cv2.warpAffine(img_formatada, M, (altura, largura))

cv2.imshow("90", rotaçao_90)

M = cv2.getRotationMatrix2D(centro, 180, escala)
rotaçao_180 = cv2.warpAffine(img_formatada, M, (altura, largura))

cv2.imshow("180", rotaçao_180)

M = cv2.getRotationMatrix2D(centro, 270, escala)
rotaçao_270 = cv2.warpAffine(img_formatada, M, (altura, largura))

cv2.imshow("270", rotaçao_270)

cv2.waitKey(0)
cv2.destroyAllWindows()
