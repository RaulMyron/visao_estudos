import cv2
import numpy as np

ix1, iy1 = -1, -1
ix2, iy2 = -1, -1
ix3, iy3 = -1, -1
ix4, iy4 = -1, -1

def select_points(event,x,y, flags, *userdata):
    global ix1,iy1,ix2,iy2,ix3,iy3,ix4,iy4,counter
    print('oi')
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        # If no point is selected yet, select the first point
        if ix1 == -1 and iy1 == -1:
            ix1,iy1 = x,y
            print("First point selected: ", ix1, iy1)
        # If one point is selected, select the second point
        elif ix2 == -1 and iy2 == -1:
            ix2,iy2 = x,y
            print("Second point selected: ", ix2, iy2)
        # If two points are selected, select the third point
        elif ix3 == -1 and iy3 == -1:
            ix3,iy3 = x,y
            print("Third point selected: ", ix3, iy3)
        # If three points are selected, select the fourth point
        elif ix4 == -1 and iy4 == -1:
            ix4,iy4 = x,y
            print("Fourth point selected: ", ix4, iy4)


img = cv2.imread('../imgs/sample_unball.png')
#resize pq ta em 4k?
scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
temp = img[:]


# Create a window and bind the mouse callback function to it
cv2.namedWindow('img')
cv2.setMouseCallback('img',select_points)

while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF

    # If ESC key is pressed, exit the loop
    if k == 27:
        break
    
    # If i is pressed, clear the window, using the dummy image
    if (k == ord('i')):
        image= temp[:]
        cv2.imshow("Window", image)

    # If four points are selected and C key is pressed, crop the image using perspective transform
    elif k == ord('c') and ix4 != -1 and iy4 != -1:
        
        #warp transformation
        
        src_pts = np.array([[ix1,iy1],[ix2,iy2],[ix3,iy3],[ix4,iy4]], dtype=np.float32)
        dst_pts = np.array([[0,0],[img.shape[1]-1,0],[img.shape[1]-1,img.shape[0]-1],[0,img.shape[0]-1]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(src_pts,dst_pts)

        cropped_img = cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
        cv2.imshow('cropped',cropped_img)

cv2.destroyAllWindows()