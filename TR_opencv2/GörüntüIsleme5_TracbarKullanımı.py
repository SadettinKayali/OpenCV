import cv2
import numpy as np

def nothing(x):
    pass

image=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("IMAGE")
cv2.createTrackbar("R","IMAGE",0,255,nothing)
cv2.createTrackbar("G","IMAGE",0,255,nothing)
cv2.createTrackbar("B","IMAGE",0,255,nothing)

cv2.createTrackbar("ON/OFF","IMAGE",0,2,nothing)

while(1):
    cv2.imshow("IMAGE",image)
    
    if cv2.waitKey(1) & 0xFF==27:
        break
    R=cv2.getTrackbarPos("R","IMAGE")
    G=cv2.getTrackbarPos("G","IMAGE")
    B=cv2.getTrackbarPos("B","IMAGE")
    
    switch=cv2.getTrackbarPos("ON/OFF","IMAGE")
    if switch==1:
        image[:]=[B,G,R]
    elif switch==0:
        image[:]=0
    else:
        break        



cv2.destroyAllWindows()
