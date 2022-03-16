import cv2
import numpy as np
"""
BEYAZ ve SİYAH EKRAN OLUŞTURMA
sifir=np.zeros([300,300])
bir=np.ones([300,300])
cv2.imshow("sifir",sifir)
cv2.imshow("bir",bir)
cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

"""
camera=cv2.VideoCapture(0) # içeri yazılan sayı görüntü alınan kamerayı ifade eden sayı, default kamera ise 0 oluyor

fourrc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Sadettin.avi",fourrc,30.0,(640,480))
print("Kamera Genişliği : ",camera.get(3))
print("Kamera Yüksekliği : ",camera.get(4))
# Kamera Görüntü Boyutunu ayarlama
#camera.set(3,640)
#camera.set(4,640)

while camera.isOpened():
    ret, frame=camera.read()
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
        print("Kameradan Görüntü Okunamıyor.")
        break
    out.write(frame)
    cv2.imshow("KAMERA",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü Sonlandırıldı.")
        break   

camera.release() # Kamera Kapatılıyor.
out.release()
# cv2.waitKey(0)   
cv2.destroyAllWindows()