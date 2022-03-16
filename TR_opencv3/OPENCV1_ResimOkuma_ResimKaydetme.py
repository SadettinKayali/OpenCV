import cv2
import numpy as np
#Resim Okuma
resimOrj=cv2.imread("opencvlogo.png")  # -1 0 1 değerlerini girebiliyoruz.  1: orjinal resmi yüklüyor 0:Resmi Griye çeviriyor -1:Alfa kanalı dahil olmak üzere resmi yükler
resimGri=cv2.imread("opencvlogo.png",0)  # -1 0 1 değerlerini girebiliyoruz.  1: orjinal resmi yüklüyor 0:Resmi Griye çeviriyor -1:Alfa kanalı dahil olmak üzere resmi yükler

#Resim Görüntüleme
cv2.imshow("Resim Adi : Orjinal Resim ",resimOrj) # ilki pencere adı ikincisi açılacak değişken
cv2.imshow("Resim Adi : Gri Resim",resimGri) # ilki pencere adı ikincisi açılacak değişken



#Resim Kaydetme
cv2.imwrite("openCV Logosu Gri.png",resimGri)

a=cv2.waitKey(0)   # Açılan ekranın beklemesini sağlıyor, herhangi bir tuşa basana kadar. Bunu bir değişkene tanımlanırsa basılan tuşu hexadecimal olarak kaydeder.
if a ==27: # 27 sayısı Hexadecimal olarak ESC tuşuna denk gelmektedir.
    cv2.destroyAllWindows()  # Herhangi bir tuşa basılana kadar ekranlar açık kalıyor. istenilen tuşa göre ayarlamak için içerisine yazmak gerekir.
elif a==ord("s"): # ord fonksiyonu ile  s tuşuna basıldığında direkt pythonun anlamasını sağlıyor.
    cv2.imwrite("openCV_otomSave.png",resimOrj)
    