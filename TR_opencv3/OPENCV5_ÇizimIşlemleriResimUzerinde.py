import cv2
import numpy as np

image=np.zeros((512,512,3),np.uint8)  # X:512 Y:512 3:RGB 3 kanallı renkli
cv2.imshow("KARANLIK",image)
# BGR = B (255,0,0) G(0,255,0)  R(0,0,255)

imageLine=cv2.line(image,(0,0),(512,512),(255,0,0),5)
cv2.imshow("MaviCizgili",imageLine)

imageRectangle=cv2.rectangle(image,(12,12),(500,500),(0,255,0),6)
cv2.imshow("KARE",imageRectangle)

imageCircle=cv2.circle(image,(256,256),100,(0,0,255),-7)
cv2.imshow("DAIRE",imageCircle)

imageText=cv2.putText(image,"SADETTIN",(100,256),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5,cv2.LINE_AA)
cv2.imshow("SADETTİN YAZISI",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()