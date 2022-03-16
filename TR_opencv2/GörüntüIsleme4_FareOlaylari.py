import cv2
from cv2 import EVENT_LBUTTONDBLCLK
from matplotlib.pyplot import draw
"""
for i in dir(cv2):
    if 'EVENT' in i:
        print(i)
EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY 
EVENT_FLAG_LBUTTON 
EVENT_FLAG_MBUTTON 
EVENT_FLAG_RBUTTON 
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK
EVENT_LBUTTONDOWN  
EVENT_LBUTTONUP    
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN  
EVENT_MBUTTONUP    
EVENT_MOUSEHWHEEL  
EVENT_MOUSEMOVE
EVENT_MOUSEWHEEL
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN
EVENT_RBUTTONUP
"""
import numpy as np

"""
# Mouse sol tık basınca daire çizdirmek
def draw(event,x,y,flags,param):
    print(x,y)
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),50,(255,0,0),-3)
    pass
""" 

drawing=False
mod=False
xi,yi=-1,-1

def draw(event,x,y,flags,param):
    global drawing,xi,yi,mod
    
    # Sol tıka basınca çizim yapmaya başlıyor. xi,yi=x,y oluyor.
    if event==cv2.EVENT_LBUTTONDOWN:
        xi,yi=x,y
        drawing=True
    # Mouse tıklanık halde olduğu için    
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mod:
                cv2.circle(image,(x,y),3,(100,150,200),-2)
            else:
                cv2.rectangle(image,(xi,yi),(x,y),(0,0,255),-3)
        else:
            pass
    # Mouse tıklanmayık halde olduğunda
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mod:
            cv2.circle(image,(x,y),3,(100,150,200),-2)
        else:
            cv2.rectangle(image,(xi,yi),(x,y),(0,0,255),-3)




image=np.ones((512,512,3),np.uint8)

cv2.namedWindow("PAINT")
cv2.setMouseCallback("PAINT",draw)

while(1):
    cv2.imshow("PAINT",image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod

cv2.destroyAllWindows()