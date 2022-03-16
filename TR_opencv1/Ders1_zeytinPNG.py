import cv2
import numpy as np

ImageOil=cv2.imread("Resimler/Zeytin.jpg") # resmin açılması için
ImageOilGrey=cv2.cvtColor(ImageOil,cv2.COLOR_BGR2GRAY) # renk dönüşümü yapılması için

cv2.imshow("Zeytin Fotosu",ImageOil)   # Orjinal resim 3 kanallı RGB red-green-blue
cv2.imshow("Zeytin Fotosu Gri",ImageOilGrey) # Gri resim 1 kanallı Grey

size_y=ImageOil.shape[0]  # yükseklik
size_x=ImageOil.shape[1]  # genişlik
kanal =ImageOil.shape[2]  # kanal sayısı, sadece renkli resimlerde 3 RGB

size_yGri=ImageOilGrey.shape[0]  # yükseklik
size_xGri=ImageOilGrey.shape[1]  # genişlik
#kanalGri =ImageOilGrey.shape[2]  # kanal sayısı, sadece renkli resimlerde 1   Hata veriyor

print("Yükseklik : ",size_y,"Genişlik : ",size_x,"Renk Kanalı Sayısı : ",kanal)
print("Yükseklik : ",size_yGri,"Genişlik : ",size_xGri)

print(ImageOil[(100,100)])  # Row 100 column 100 deki pikseli renkli olduğu için 3 kanalda gösteriyor
print(ImageOilGrey[(100,100)]) # Row 100 column 100 deki pikseli gri olduğu için 1 kanalda gösteriyor

# Açılan resimlerin kapatılana kadar gösterilmesi için gereken kodlar
cv2.waitKey(0)
cv2.destroyAllWindows()