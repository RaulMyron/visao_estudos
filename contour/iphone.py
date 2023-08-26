import cv2

# Le imagem
image = cv2.imread('../imgs/vision.jpeg')
cv2.imshow('oi',image)
# converte para Grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
"""
 Agora, usa-se a funcao threshold() (relativo ao limite binário)
 Qualquer pixel com um valor > 150 será definido como um valor de 255 (branco).
 Todos os pixels restantes na imagem resultante serão definidos como 0 (preto).
 O valor limite de 150 é um parâmetro ajustável.
"""
# Aplicando limite binario
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# visualize a imagem binária usando a imshow()
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# A imagem está com todos contornos em cor branca
# agora, podemos aplicar o algoritmo para desenhar contornos( CHAIN_APPROX_NONE)

# Detecta contornos na imagem binaria usadno cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# Desenha contornos na imagem original
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# Mostra os resultados
cv2.imshow('countours',image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

