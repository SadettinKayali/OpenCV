import os  # Operating sistem kütüphanesi, verileri diskten almak için eklendi ve kullanılacak.
import cv2 # Computer Vision 2 kütüphanesi görüntü işleme için eklendi.
import matplotlib.pyplot as plot
import numpy as np

ImageAdress=os.listdir("DataSet")
image=cv2.imread("DataSet/",ImageAdress[0])
image=cv2.resize(image,(500,500))

plot.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plot.show()
