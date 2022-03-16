import cv2
import numpy as np

# capture=cv2.VideoCapture("VideoAdi.avi")  # Eğer videodan yakalamalar yapılacaksa bu kullanılıyor.
capture=cv2.VideoCapture(0)  # Webcamdan görüntü alacağı anlaşılıyor. 0 yazıldığı için


while (True):
    # Degisken tutucu 0 veya 1
    DegerTutucu, frame=capture.read() # Tutulan değişken okunuyor ve yeni bir değişkene atanıyor.
    frame=cv2.rectangle(frame,(150,150),(350,350),(0,255,0))
    
    cv2.imshow("KAMERA ",frame)  # Frame her seferinde gösteriliyor.
    
    
    
    #Degisken=cv2.waitKey(0)          # 0 yazarsak tek bir kare gösteriyor tuşa bastıkça gösterilen kare değişiyor.
    Degisken=cv2.waitKey(1)           # 1 yazarsak akıcı şekilde kamera çalışıyor.
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break


capture.release()

cv2.destroyAllWindows()