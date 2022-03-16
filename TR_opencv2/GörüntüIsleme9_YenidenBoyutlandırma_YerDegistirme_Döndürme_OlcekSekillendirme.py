import cv2
import numpy as np

image=cv2.imread("opencvlogonew.png")

#resize1=cv2.resize(image,(300,300))
#resize1=cv2.resize(image,None,fx=3,fy=2)
#resize1=cv2.resize(image,None,fx=3,fy=2,interpolation=cv2.INTER_CUBIC)
#cv2.imshow("resize1",resize1)

print(image.shape)
#rows,columns,Color=image.shape
rows,columns=image.shape[:2]
"""
## İLERİ GERİ TAŞIMA
#translation_matrix=np.float32([[1,0,50],[0,1,50]])
#translation_matrix=np.float32([[1,0,100],[0,1,25]])
#translation_matrix=np.float32([[1,0,-100],[0,1,25]])
translation_matrix=np.float32([[1,0,25],[0,1,25]])
image_translation=cv2.warpAffine(image,translation_matrix,(columns+50,rows+50))
#cv2.imshow("image_translation",image_translation)
## (rows,columns) => (columns,rows) olarak yazılıyor
## SAĞA SOLA DÖNDÜRME
#rotation_matrix=cv2.getRotationMatrix2D((columns/2,rows/2),-30,0.5)
rotation_matrix=cv2.getRotationMatrix2D((columns/2,rows/2),30,1)
image_rotation=cv2.warpAffine(image,rotation_matrix,(columns,rows))
#image_rotation=cv2.warpAffine(image,rotation_matrix,(int(columns*1.7),int(rows*0.7)))
#cv2.imshow("image_rotation",image_rotation)
## EĞİK ŞEKİLDE TAŞIMA YERLEŞTİRME
search_points=np.float32([[0,0],[columns-1,0],[0,rows-1]])
search_points_new=np.float32([[0,0],[int(0.5*(columns-1)),0],[int(0.5*(columns-1)),rows-1]])
affine_matrix=cv2.getAffineTransform(search_points,search_points_new)
image_output=cv2.warpAffine(image,affine_matrix,(columns,rows))

cv2.imshow("image",image)
cv2.imshow("image_output",image_output)

"""

search_points1=np.float32([
    [0,0]       ,[columns-1,0],
    [0,rows-1]  ,[columns-1,rows-1]
])
search_points_new1=np.float32([
    [0,0]       ,[columns-1,0],
    [int(0.33*(columns-1)),rows-1]  ,[int(0.66*(columns-1)),rows-1]
])

projective_matrix=cv2.getPerspectiveTransform(search_points1,search_points_new1)
image_output1=cv2.warpPerspective(image,projective_matrix,(columns,rows))


cv2.imshow("image",image)
cv2.imshow("image_output",image_output1)



cv2.waitKey()
cv2.destroyAllWindows
