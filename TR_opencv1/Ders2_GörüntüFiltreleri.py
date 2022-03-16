import cv2
import numpy as np
# FİLTRELEME İŞLEMLERİ ÖRNEKLERİ
ImageOil2=cv2.imread("Resimler/Zeytin2.jpg") # resmin açılması için
"""
BULANIKLAŞTIRMA İŞLEMİ
kernel=np.ones((10,10),np.float32)/100  # Row x Column kaç ise çarpımına bölüyoruz.    # r x c  3x3 pikselde bulanıklaştırma yapıldığı için      # bulanıklaştırma işleminde kullanılabilir.
blur=cv2.filter2D(ImageOil2,-1,kernel) # Oluşturulan kernel ile bulanıklaştırma
blur2=cv2.blur(ImageOil2,(3,3))    # Hazır fonksiyon ile bulanıklaştırma

print(kernel)

cv2.imshow("Zeytin Fotosu",ImageOil2)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Blur",blur)
cv2.imshow("Zeytin Fotosu Blur2",blur2)

"""

"""
KESKİNLEŞTİRME İŞLEMİ
kernel=np.array([[-1,-1,-1],
                 [-1,9,-1],
                 [-1,-1,-1]])

keskinlestirme=cv2.filter2D(ImageOil2,-1,kernel)  # -1 orjinal resmin derinliği ile aynı anlama geliyor.

cv2.imshow("Zeytin Fotosu",ImageOil2)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Keskinlestirilmis",keskinlestirme)

"""
"""
GAUSSİAN BLUR    kenarları da bulanıklaştırma eğiliminde
gaus=cv2.GaussianBlur(ImageOil2,(5,5),0)   # 0 yazınca x standart sapmasını 0 alarak orjinal resim çekirdeğini kullanıyor.

cv2.imshow("Zeytin Fotosu",ImageOil2)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Gaussian Blur",gaus)

"""
"""
Bilateral Blur   kenarları biraz daha keskin bırakıyor
bilateral=cv2.bilateralFilter(ImageOil2,9,75,75)  

cv2.imshow("Zeytin Fotosu",ImageOil2)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Bilateral Blur",bilateral)

"""
"""
Median Blur (median)   daha temiz görüntü oluşur, komşu piksellerin ortalamasını alarak filtreler
ImageOil=cv2.imread("Resimler/Zeytin.jpg")

median=cv2.medianBlur(ImageOil,11,)   # tek sayı veriyoruz

cv2.imshow("Zeytin Fotosu",ImageOil)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Median Blur",median)

"""

"""
Canny   kenarları tespit etme
"""
ImageOil=cv2.imread("Resimler/Zeytin.jpg")

canny=cv2.Canny(ImageOil,10,1000)   # tek sayı veriyoruz

cv2.imshow("Zeytin Fotosu",ImageOil)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Canny",canny)

# Açılan resimlerin kapatılana kadar gösterilmesi için gereken kodlar
cv2.waitKey(0)
cv2.destroyAllWindows()