import cv2
import numpy as np
from matplotlib import pyplot as plot

def detectFromImage(imageRead):
    image=cv2.imread(imageRead)
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_frontalface_default.xml")
    faces=face_cascade.detectMultiScale(gray_scale,1.2,2)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),4)
        
    cv2.imshow("BASLIK",image)
    print(faces)
    cv2.waitKey(0)
    print("Program Kapatılıyor.")
    cv2.destroyWindow("BASLIK")
"""
image=cv2.imread("Kisilerim.jpg")
print("Orjinal Resim Piksel : ",image.shape)
#print(image.size)

# Griye çevirme sebeplerinden birisi kullanılan hafızayı azaltmak.
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("Grileştirilmiş Piksel",gray_scale.shape)
#print(gray_scale.size)

face_cascade=cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(gray_scale,1.2,5) # ölçek değeri,Minimum komşu sayısı,komşu sayısı değiştirilerek bulunan yüz değişiyor.
print(faces)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)

cv2.imshow("Face Detection",image)
cv2.waitKey(0)
cv2.destroyWindow()
"""

"""
titlelist=["IMAGE","IMAGE_Gray"]
imagelist=[image,gray_scale]


for i in range(2):
    plot.subplot(2,1,i+1)
    plot.imshow(imagelist[i],"gray",vmin=0,vmax=255)
    plot.title(titlelist[i])
    plot.xticks([]),plot.yticks([])

#plot.imshow(image)
#plot.imshow(gray_scale)
plot.show()
"""
detectFromImage("Kisilerim.jpg")




