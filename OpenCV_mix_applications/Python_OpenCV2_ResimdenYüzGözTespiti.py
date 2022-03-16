import cv2

def detected_Face_Eyes_From_Image(imageRead):
    face_cascade=cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_frontalface_default.xml")
    eye_cascade=cv2.CascadeClassifier("OpenCV_Dosyalar_Kodlar\haarcascade_eye.xml")
    image=cv2.imread(imageRead)
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_scale,1.2,3)
    for(xFace,yFace,weightFace,heightFace) in faces:
        cv2.rectangle(image,(xFace,yFace),(xFace+weightFace,yFace+heightFace),(0,255,0),4)
        # ROI : Region on Interest
        ROI_gray=gray_scale[yFace:yFace+heightFace,xFace:xFace+weightFace]
        ROI_color=image[yFace:yFace+heightFace,xFace:xFace+weightFace]
        eyes=eye_cascade.detectMultiScale(ROI_gray,1.1,2)
        for(xEye,yEye,weightEye,heightEye) in eyes:
            cv2.rectangle(ROI_color,(xEye,yEye),(xEye+weightEye,yEye+heightEye),(255,0,0),2)
    cv2.imshow("Faces and Eyes Detected",image)
    print("Faces : ",faces)
    print("Eyes  : ",eyes)
    cv2.waitKey(0)
    print("Program Kapatılıyor.")
    cv2.destroyAllWindows()




detected_Face_Eyes_From_Image("Kisilerim.jpg")