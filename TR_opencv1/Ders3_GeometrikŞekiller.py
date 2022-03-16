import cv2

import os
ImageFile = os.path.join(os.path.dirname(__file__), 'Resimler\Zeytin.jpg')
assert os.path.exists(ImageFile)

ImageOlive=cv2.imread(ImageFile)

#ImageOlive=cv2.imread("Resimler\Zeytin.jpg")
#cv2.imwrite("ZeytinGri.jpg",ImageOlive) # Anlık görüntü kaydetmek için kullanılabilir. # Dosya kaydetmek için kullanılır.

cv2.line(ImageOlive,(0,0),(500,500),(150,120,10),15) # Başlangıç ve bitiş koordinatları yazılıyor. RGB olarak renk kodu yazılıyor. Çizgi kalınlığı yazılıyor
cv2.rectangle(ImageOlive,(120,120),(360,560),(255,150,50),2) #başlangıç noktası, genişlik ve yükseklik,kalınlık (içini doldurmak için - li yazılıyor)
cv2.rectangle(ImageOlive,(720,10),(160,160),(50,150,255),-4) #başlangıç noktası, genişlik ve yükseklik,kalınlık (içini doldurmak için - li yazılıyor)
cv2.circle(ImageOlive,(150,650),100,(50,60,70),9) #başlangıç noktası, çap ,kalınlık (içini doldurmak için - li yazılıyor)
cv2.circle(ImageOlive,(550,650),100,(150,160,170),-9)
cv2.ellipse(ImageOlive,(500,500),(100,200),0,0,360,(0,122,255),7)#başlangıç noktası, genişlik ve yükseklik,açısı,kaç derece çizdirsin,kalınlık (içini doldurmak için - li yazılıyor)
cv2.ellipse(ImageOlive,(500,100),(200,100),45,0,120,(255,122,0),-7)#başlangıç noktası, genişlik ve yükseklik,açısı,kaç derece çizdirsin,kalınlık (içini doldurmak için - li yazılıyor)
cv2.putText(ImageOlive,'Sadettin',(100,0),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(100,100,100),3,cv2.LINE_AA,True) # True olursa aynalanmış yazar,
cv2.putText(ImageOlive,'KAYALI',(0,200),cv2.FONT_ITALIC,3,(200,200,200),9,cv2.LINE_AA,False)# False olursa düz yazar,


cv2.imshow("Zeytin Fotosu",ImageOlive)



cv2.waitKey(0)  # klavyeden bir tuşa basılmasını istiyor.
cv2.destroyAllWindows("Zeytin Fotosu") # pencerenin kapatılmasını sağlıyor. İçine ne yazılırsa onu kapatır. Yazılmazsa hepsini kapatır

