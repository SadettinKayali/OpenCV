import cv2
import numpy as np

# capture=cv2.VideoCapture("VideoAdi.avi")  # Eğer videodan yakalamalar yapılacaksa bu kullanılıyor.
capture=cv2.VideoCapture(0)  # Webcamdan görüntü alacağı anlaşılıyor. 0 yazıldığı için

# cv2.imshow("Sado",capture)

# Birden fazla kareyi göstermek gerekiyor.
while (True):
    # Degisken tutucu 0 veya 1
    DegerTutucu, frame=capture.read() # Tutulan değişken okunuyor ve yeni bir değişkene atanıyor.
    cv2.imshow("Pencere Adi ",frame)  # Frame her seferinde gösteriliyor.
    #Degisken=cv2.waitKey(0)          # 0 yazarsak tek bir kare gösteriyor tuşa bastıkça gösterilen kare değişiyor.
    Degisken=cv2.waitKey(1)           # 1 yazarsak akıcı şekilde kamera çalışıyor.
    if Degisken==27 :       # Eğer tuş ESC ise döngü kapatılıyor. 27 hexadecimal olarak ESC tuşuna denk geliyormuş.
        break
    # ord("İstenilen Tuş") komutu kullanılarak istenilen tuş ayarlanabilir.
    """
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break
    # buradaki olay basılan tuşu hexadecial a çevirip ord() fonksiyonu ile doğruluğunu kontrol etmek
    """
    
    
capture.release()

cv2.destroyAllWindows()