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
        
    print(counter)
 
image = cv2.imread("../imgs/card.jpeg")
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
        
        #sei lá de onde eu tirei esse metodo de dst_pts, mas functiona, vo falar oq 
        src_pts = np.array([[ix1,iy1],[ix2,iy2],[ix3,iy3],[ix4,iy4]], dtype=np.float32)
        dst_pts = np.array([[0,0],[image.shape[1]-1,0],[image.shape[1]-1,image.shape[0]-1],[0,image.shape[0]-1]], dtype=np.float32)
        
        M = cv2.getPerspectiveTransform(src_pts,dst_pts)
        image = cv2.warpPerspective(image,M,(image.shape[1],image.shape[0]))
        
        #cv2.imshow('cropped',cropped_img)

 
cv2.destroyAllWindows()