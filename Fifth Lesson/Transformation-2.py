#RESMİ DÖNDÜRMEK
import cv2 as cv
import numpy as np

def rotate(img,angle,rotPoint=None): #Çoğu durumda resmi merkezinden döndürmek istersin; kullanıcı ekstra bir şey yazmasın diye varsayılan olarak merkez kullanılıyor. rotPoint opsiyonel
    (height,width) = img.shape[:2] # Görüntünün boyutlarını alır.

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0) #OpenCV’de pozitif değerler saat yönünün tersine (CCW) döndürür.
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

rotated1 = rotate(parkImage,90)
cv.imshow("Rotated-1",rotated1)

rotated2 = rotate(parkImage,45)
cv.imshow("Rotated-2",rotated2)

rotated3 = rotate(parkImage,-45)
cv.imshow("Rotated-3",rotated3)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()