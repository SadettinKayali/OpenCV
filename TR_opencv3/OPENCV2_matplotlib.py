import cv2
import numpy as np
from matplotlib import pyplot as plot  # matplotlib'den pyplot u çağır ve plot olarak kullanabileyim.

image=cv2.imread("opencvlogo.png",0)

plot.imshow(image,cmap="gray",interpolation="bicubic")
#plot.xticks([]) , plot.yticks([])  # x ve ye değerlerini göstermesin diye boş küme atandı.
plot.show()
