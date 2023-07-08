import cv2
import numpy as np
 
top_left_corner, bottom_right_corner, counter=0,0,0
counter = 0
top_left_corner=[]
bottom_right_corner=[]

from tkinter import messagebox

ix1, iy1 = -1, -1 #a
ix2, iy2 = -1, -1 #b
ix3, iy3 = -1, -1 #c 
ix4, iy4 = -1, -1 #d

color = (0, 255, 0)
thickness = 3

# function which will be called on mouse input
def drawRectangle(action, x, y, flags, *userdata):

    # Mark the top left corner when left mouse button is pressed
    global top_left_corner, bottom_right_corner, counter, a, b, c, d
    global ix1,iy1,ix2,iy2,ix3,iy3,ix4,iy4, color, thickness
    global image 
    
    if action == cv2.EVENT_LBUTTONDOWN:
        
        
        top_left_corner = [(x,y)]
        
        if counter==0:
            ix1,iy1 = x,y
            print("First point selected: ", ix1, iy1)
            counter+=1
            
        elif counter==1:
            ix2,iy2 = x,y
            print("Second point selected: ", ix2, iy2)
            cv2.line(image,(ix1,iy1),(x,y),color,thickness)    
            cv2.imshow("Window",image)
            counter+=1
            
        elif counter==2:
            ix3,iy3 = x,y
            print("Third point selected: ", ix3, iy3)
            cv2.line(image,(ix2,iy2),(x,y),color,thickness)  
            cv2.imshow("Window",image)
            counter+=1

        elif counter==3:
            ix4,iy4 = x,y
            print("Fourth point selected: ", ix4, iy4)
            cv2.line(image,(ix3,iy3),(x,y),color,thickness)
            cv2.line(image,(x,y),(ix1,iy1),color,thickness)
            cv2.imshow("Window",image)
            counter+=1

        elif counter==4:
            counter=0
            print('limite, clique mais uma vez para remcomecar')
            
            image = temp.copy()
            cv2.imshow("Window", image)
                        
            messagebox.showinfo('Aviso', \
                'Clique mais uma vez para reiniciar')

            ix1, iy1 = -1, -1 #a
            ix2, iy2 = -1, -1 #b
            ix3, iy3 = -1, -1 #c 
            ix4, iy4 = -1, -1 #d
        
    #print(counter) qtd de vezes 
 
def normalize_pixel_value(pixel_value, min_pixel_value, max_pixel_value):
    normalized_value = (pixel_value - min_pixel_value) / (max_pixel_value - min_pixel_value)
    return round(normalized_value, 16)
     

image = cv2.imread("../imgs/sample_unball.png")

scale_percent = 30
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

temp = image.copy()

cv2.namedWindow("Window")
cv2.setMouseCallback("Window", drawRectangle)

k=0

while k!=113:
    # Display the image
    cv2.imshow("Window", image)
    k = cv2.waitKey(0)
    # If c is pressed, clear the window, using the dummy image
    if (k == 99):
        image = temp.copy()
        counter = 0
        messagebox.showinfo('Aviso', \
                    'Reiniciando')
        cv2.imshow("Window", image)

    elif k == ord('w') and ix4 != -1 and iy4 != -1:

        messagebox.showinfo('WARPING', \
                    'WARPING')
        
        dst_pts = np.array([[0,0],[image.shape[1]-1,0],[image.shape[1]-1,image.shape[0]-1],[0,image.shape[0]-1]], dtype=np.float32)
        src_pts = np.array([[ix1,iy1],[ix2,iy2],[ix3,iy3],[ix4,iy4]], dtype=np.float32)
        
        height, width, _ = image.shape
    
        base = np.array([[0,0],[1,0],[1,1],[0,1]])
        
        #[(0.1289304826416534, 0.22905718122209823), (0.6941748617054804, 0.19912401471819197), (0.6305899650427946, 0.697082257952009), (0.10528110901008493, 0.7111135428292411)]
        src_pts_malp = []
        
        for i in src_pts:
            x = normalize_pixel_value(i[0],0,image.shape[1])
            y = normalize_pixel_value(i[1],0,image.shape[0])
            src_pts_malp.append((x,y))
        
        key_points = np.array(src_pts_malp) * np.array([width, height])
        frame_points = base * np.array([width, height])
        
        M = cv2.getPerspectiveTransform(src_pts,dst_pts)
        h, mask = cv2.findHomography(key_points, frame_points, cv2.RANSAC)
        #h ou M H-> malp M->BINGAI
        
        print(h)
        print(M)
        
        points = np.array 
        image = cv2.warpPerspective(image, h, (image.shape[1], image.shape[0]))
        #image = cv2.warpPerspective(image,M,(image.shape[1],image.shape[0]))

 
cv2.destroyAllWindows()