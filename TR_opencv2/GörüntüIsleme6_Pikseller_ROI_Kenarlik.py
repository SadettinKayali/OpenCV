import cv2
import numpy as np
from matplotlib import pyplot as plot 

#print(image.shape)
#print(image.size)
#print(image.dtype)
#print(image[100,100])
"""
image=cv2.imread("AKINCI_tiha.jpg")
crop=image[500:800,500:800] # Resimi kırpmak
image[100:400,1400:1700]=crop # Kırpılan resimi mevcut resmin üstüne eklemek

plot.subplot(221)
plot.imshow(image)
plot.subplot(222)
plot.imshow(crop)

imageG=cv2.imread("AKINCI_tiha.jpg",0)
cropG=imageG[500:800,500:800] # Resimi kırpmak
imageG[100:400,1400:1700]=cropG # Kırpılan resimi mevcut resmin üstüne eklemek

plot.subplot(223)
plot.imshow(imageG,"gray")
plot.subplot(224)
plot.imshow(cropG,"gray")
"""
##############################################################
"""
image=cv2.imread("AKINCI_tiha.jpg")


image[:,:,(0,1)]=0
cv2.imshow("RED",image)

image=cv2.imread("AKINCI_tiha.jpg")
image[:,:,(1,2)]=0
cv2.imshow("BLUE",image)

image=cv2.imread("AKINCI_tiha.jpg")
image[:,:,(0,2)]=0
cv2.imshow("GREEN",image)
"""
##############################################################

image4=cv2.imread('opencvlogo.png')
replicate=cv2.copyMakeBorder(image4,100,100,100,100,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(image4,100,100,100,100,cv2.BORDER_REFLECT)
reflect_101=cv2.copyMakeBorder(image4,100,100,100,100,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(image4,100,100,100,100,cv2.BORDER_WRAP)
BLUE=[0,0,255]
constant=cv2.copyMakeBorder(image4,50,50,50,50,cv2.BORDER_CONSTANT,value=BLUE)

plot.subplot(231),plot.imshow(image4,'gray'),plot.title('ORIGINAL')
plot.subplot(232),plot.imshow(replicate,'gray'),plot.title('REPLICATE')
plot.subplot(233),plot.imshow(reflect,'gray'),plot.title('REFLECT')
plot.subplot(234),plot.imshow(reflect_101,'gray'),plot.title('REFLECT_101')
plot.subplot(235),plot.imshow(wrap,'gray'),plot.title('WRAP')
plot.subplot(236),plot.imshow(constant,'gray'),plot.title('CONSTANT_BLUE')


plot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()