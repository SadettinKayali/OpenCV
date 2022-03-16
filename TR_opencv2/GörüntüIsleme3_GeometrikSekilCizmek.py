import cv2
from cv2 import ellipse
from cv2 import line
import numpy as np

image=np.zeros((512,512,3),np.uint8) #uint8 tam sayı değerleri alması için , 3: BGR değerleri alması için

cv2.line(image,(0,0),(512,512),(255,0,0),5)
cv2.line(image,(512,0),(0,512),(0,255,0),10)

cv2.rectangle(image,(64,64),(448,448),(0,0,255),5)
cv2.rectangle(image,(128,128),(384,384),(0,0,255),-5)

cv2.ellipse(image,(256,256),(200,150),0,0,180,(255,100,0),5)
cv2.ellipse(image,(256,256),(200,150),0,180,360,(0,100,255),-5)

cv2.circle(image,(256,256),60,(120,120,120),3)
cv2.circle(image,(256,256),30,(220,220,220),-3)

points=np.array([[256,0],[0,256],[256,512],[512,256]],np.int32)
points2=points.reshape(-1,1,2)

cv2.polylines(image,[points],True,(255,255,255),2)
# True yazılırsa çizgileri birleştirip kapalı hale getiriyor
# False yazılırsa açık çizgi olarak birleştiriyor.

font=cv2.FONT_HERSHEY_COMPLEX
line=cv2.LINE_AA
cv2.putText(image,'OpenCV',(64,256),font,3,(0,0,0),2,line)


cv2.imshow("IMAGE",image)
cv2.waitKey(0)
cv2.destroyAllWindows()