import cv2
import numpy as np
from matplotlib import pyplot as plot

imageGri=cv2.imread("Resimler\Zeytin3.jpg",0)   # sondaki 0 ı kaldırınca değişirince resim değişiyor. 0 olunca gri oluyor
esik,thresh1=cv2.threshold(imageGri,80,255,cv2.THRESH_BINARY)
esik,thresh2=cv2.threshold(imageGri,80,255,cv2.THRESH_BINARY_INV)
esik,thresh3=cv2.threshold(imageGri,80,255,cv2.THRESH_OTSU)
esik,thresh4=cv2.threshold(imageGri,80,255,cv2.THRESH_TOZERO)
esik,thresh5=cv2.threshold(imageGri,80,255,cv2.THRESH_TOZERO_INV)
esik,thresh6=cv2.threshold(imageGri,80,255,cv2.THRESH_TRUNC)

titlelist=["BINARY","BINARY_INV","OTSU","TOZERO","TOZERO_INV","TRUNC"]
imagelist=[thresh1,thresh2,thresh3,thresh4,thresh5,thresh6]


# Belirlenen eşik değerinin altındaki ve üstündeki değerlere göre çeşitli eşik değerleri verilebiliyor. Her piksel için ayrı ayrı eşikleme değeri yapılıyor.

for i in range(6):
    plot.subplot(2,3,i+1)
    plot.imshow(imagelist[i],"gray",vmin=0,vmax=255)
    plot.title(titlelist[i])
    plot.xticks([]),plot.yticks([])
plot.show()









cv2.waitKey(0)
cv2.destroyAllWindows()
