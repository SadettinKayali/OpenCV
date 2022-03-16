import cv2
from matplotlib import pyplot as plot

resim=cv2.imread("KizKulesi.jpg")

# cv2.namedWindow("resim",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

cv2.imshow("resim",resim)
cv2.imshow("Resim Penceresi",resim)

plot.imshow(resim,cmap="gray")
plot.show()

key=cv2.waitKey(0)

if key==27:
    print("ESC tuşuna basıldı.")
elif key == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi.")
    cv2.imwrite("kizkulesigri.jpg",resim)

# cv2.destroyWindow("Resim Penceresi")
cv2.destroyAllWindows()