import cv2
# IP webcam uygulaması yükleniyor.
# Start server butonuna basılıyor.
# Kamera açılınca alttaki IP adresini url değişkenine yazıyoruz.
# Bilgisayar ve telefonun aynı wifi ağına bağlı olması lazım.
# internet yoksa bile HotSpot ile telefondan ve ya bilgisayardan paylaşım açıp aynı ağ üzerine bağlanmalıdır.


url="http://192.168.1.100:8080/video"
camera=cv2.VideoCapture(url)

while camera.isOpened():
    ret,frame=camera.read()
    
    if not ret:
        print("Kameradan görüntü okunamıyor !")
        
    cv2.imshow("Görüntü",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
cv2.destroyAllWindows()