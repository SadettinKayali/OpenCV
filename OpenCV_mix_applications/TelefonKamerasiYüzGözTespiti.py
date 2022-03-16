import cv2
import numpy as np

url="http://192.168.1.100:8080/video"

face_cascade=cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_frontalface_default.xml")
eye_cascade =cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_eye.xml")

camera=cv2.VideoCapture(url)

while camera.isOpened():
    ret,image=camera.read()
    
    if not ret:
        print("Kameradan görüntü okunamıyor !")
        
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.2,3)
    
    for (xF,yF,wF,hF) in faces:
        cv2.rectangle(image,(xF,yF),(xF+wF,yF+hF),(255,0,0),4)
        ROI_gray =gray[yF:yF+hF,xF:xF+wF]
        ROI_color=image[yF:yF+hF,xF:xF+wF]
        eyes=eye_cascade.detectMultiScale(ROI_gray,1.1,2)
        for (xE,yE,wE,hE) in eyes:
            cv2.rectangle(ROI_color,(xE,yE),(xE+wE,yE+hE),(0,0,255),2)
        
    cv2.imshow("Detedted : ",image)
    # 0 yapınca tusa bastıkca okuma yapıyor. 1 ve üzeri yapınca akıcı oldu 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        break
cv2.destroyAllWindows()

