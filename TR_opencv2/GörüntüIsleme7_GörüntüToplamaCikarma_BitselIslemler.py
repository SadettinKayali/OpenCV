import cv2
import numpy as np
"""
x=np.uint8([250])
y=np.uint8([10])

print(x+y)
print(cv2.add(x,y))
"""

"""
image1=cv2.imread("piksel640x640_1.png")
image2=cv2.imread("piksel640x640_2.png")
toplam=cv2.addWeighted(image1,0.8,image2,0.2,0)

cv2.imshow("IMAGE1",image1)
cv2.imshow("IMAGE2",image2)
cv2.imshow("IMAGE TOPLAM",toplam)
"""
# İşlem yapılacak resimler okundu.
image1=cv2.imread("opencvlogosiyah.jpg")
image2=cv2.imread("AKINCI_tiha.jpg")
# İşlem yapılacak resimlerin matris türünden boyutları okundu.
print("opencvlogosiyah: ",image1.shape)
print("AKINTI_tiha piksel:", image2.shape)
# 2. resimden(büyük olan) Yerleştirmek istediğimiz bölgeden 1. resim kadar alanı kırpıyoruz. 
x,y,z=image1.shape
ROI=image2[0:x,0:y]
# 1. resmi grileştirme işlemi yapıyoruz.
image1_gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# 1. resme eşikleme işlemi uyguluyoruz. 10 pikselin altındaki değerleri 0 a , 10 pikselin üstündeki değerleri 255 e yükseltiyoruz.
ret,mask=cv2.threshold(image1_gray,10,255,cv2.THRESH_BINARY)
# yapmış olduğumuz maskeyi ters çeviriyoruz. 0 => 1  1=>0
mask_inv=cv2.bitwise_not(mask)
# Bitsel çarpımı yapıyoruz. Renkli olduğu için iki tarafada ROI değerini giriyoruz.
image1_bg=cv2.bitwise_and(ROI,ROI,mask=mask_inv)
image2_fg=cv2.bitwise_and(image1,image1,mask=mask)
# Bitsel çarpımlar yapıldıktan sonra iki değişkeni topluyoruz.
toplam=cv2.add(image1_bg,image2_fg)
# toplam değerini ana resimdeki yerine ekliyoruz.
image2[0:x,0:y]=toplam

# YAPILAN İŞLEMLERİN GÖSTERİLİMİ
cv2.namedWindow("IMAGE2",cv2.WINDOW_NORMAL)

cv2.imshow("IMAGE1",image1)
cv2.imshow("IMAGE1_GRAY",image1_gray)
cv2.imshow("IMAGE_gray MASK",mask)
cv2.imshow("IMAGE_gray MASK_INV",mask_inv)
cv2.imshow("IMAGE1_bg",image1_bg)
cv2.imshow("IMAGE1_fg",image2_fg)
cv2.imshow("IMAGE1_bg+IMAGE2_fg",toplam)
cv2.imshow("IMAGE2",image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
