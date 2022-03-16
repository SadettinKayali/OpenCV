import cv2
import numpy as np

image=cv2.imread("KizKulesi.jpg")
print(image.shape)
rows,columns=image.shape[:2]

click_count=0
Liste=[]

WantedPoints=np.float32([
    [0,0],         [columns-1,0],
    [0,rows-1],    [columns-1,rows-1]])

cv2.namedWindow("IMAGE",cv2.WINDOW_NORMAL)
cv2.namedWindow("IMAGE OUTPUT",cv2.WINDOW_NORMAL)
def draw(event,x,y,flags,param):
    global click_count,Liste
    
    if click_count<4:
        if event==cv2.EVENT_LBUTTONDBLCLK:
            #print(click_count)
            #print(x,y)
            click_count+=1
            Liste.append((x,y))
    else:
        SelectedPoints=np.float32([
            [Liste[0][0],Liste[0][1]],
            [Liste[1][0],Liste[1][1]],
            [Liste[2][0],Liste[2][1]],
            [Liste[3][0],Liste[3][1]] ])
        click_count=0
        Liste=[]
        M=cv2.getPerspectiveTransform(SelectedPoints,WantedPoints)
        ImageOutput=cv2.warpPerspective(image,M,(columns,rows))
        cv2.imshow("IMAGE OUTPUT",ImageOutput)
    pass
"""
SelectedPoints=np.float32([
    [80,100],    [400,90],
    [50,400],    [400,400]])
WantedPoints=np.float32([
    [0,0],         [columns-1,0],
    [0,rows-1],    [columns-1,rows-1]])
"""

#ProjectiveMatrix=cv2.getPerspectiveTransform(SelectedPoints,WantedPoints)
#ImageOutput=cv2.warpPerspective(image,ProjectiveMatrix,(columns,rows))
cv2.setMouseCallback("IMAGE",draw)

while(1):
    cv2.imshow("IMAGE",image)
    #cv2.imshow("IMAGE OUTPUT",ImageOutput)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()