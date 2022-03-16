import cv2
from cv2 import EVENT_LBUTTONDBLCLK
from matplotlib.pyplot import draw

import numpy as np

drawing=False
mod=False
mod1=mod
mod2=mod
mod3=mod
xi,yi=-1,-1



def draw(event,x,y,flags,param):
    global drawing,xi,yi,mod
    
    # Sol tıka basınca çizim yapmaya başlıyor. xi,yi=x,y oluyor.
    if event==cv2.EVENT_LBUTTONDOWN:
        xi,yi=x,y
        drawing=True
        #mod3==False & mod2==True & mod1==False:
        #mod3==False & mod2==False & mod1==True:
    # Mouse tıklanık halde olduğu için    
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if (mod3 & mod2)!=mod1 & mod1==True:
                cv2.circle(image,(x,y),3,(100,150,200),-2)
            elif (mod3 & mod1)!=mod2 & mod2==True:
                cv2.rectangle(image,(xi,yi),(x,y),(0,0,255),-3)
            elif (mod2 & mod1)!=mod3 & mod3==True:
                cv2.line(image,(x,y),(x,y),(255,0,0),7)
        else:
            pass
    # Mouse tıklanmayık halde olduğunda
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if (mod3 & mod2)!=mod1 & mod1==True:
            cv2.circle(image,(x,y),3,(100,150,200),-2)
        elif (mod3 & mod1)!=mod2 & mod2==True:
            cv2.rectangle(image,(xi,yi),(x,y),(0,0,255),-3)
        elif (mod2 & mod1)!=mod3 & mod3==True:
            cv2.line(image,(x,y),(x,y),(255,0,0),7)










image=np.ones((512,512,3),np.uint8)

cv2.namedWindow("PAINT")
cv2.setMouseCallback("PAINT",draw)

while(1):
    cv2.imshow("PAINT",image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("'q' is selected : Exiting the program !")
        break
    
    if cv2.waitKey(1) & 0xFF == ord("c"):
        mod2=mod
        mod3=mod
        mod1=not mod
        print("'c' is selected : Circle drawing !")
    elif cv2.waitKey(1) & 0xFF == ord("r"):
        mod1=mod
        mod3=mod
        mod2=not mod
        print("'r' is selected : Rectangle drawing !")
    elif cv2.waitKey(1) & 0xFF == ord("l"):
        mod1=mod
        mod2=mod
        mod3=not mod
        print("'l' is selected : Line drawing !")













cv2.destroyAllWindows()