import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade =cv2.CascadeClassifier("haarcascade_eye.xml")

camera=cv2.VideoCapture(0)

while True:
    ret,image=camera.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.2,3)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)
        ROI_gray =gray[y:y+h,x:x+w]
        ROI_color=image[y:y+h,x:x+w]
    
    cv2.imshow("Detedted : ",image)
    # 0 yapınca tusa bastıkca okuma yapıyor. 1 ve üzeri yapınca akıcı oldu 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
