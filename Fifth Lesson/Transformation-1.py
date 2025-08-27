#RESMİ SAĞA SOLA AŞAĞI YUKARI KAYDIRMAK
import cv2 as cv
import numpy as np

#-x --> Resmi sola kaydırır
#+x --> Resmi sağa kaydırır
#-y --> Resmi yukarı kaydırır
#+y --> Resmi aşağı kaydırır

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #Bu kısımdaki 1 ve 0'lar sabit değiştirirsen eğer resin zoom atabilir veya farklı şeyler olabilir.
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

translated1 = translate(parkImage,100,100)
cv.imshow("Translated-1", translated1)

translated2 = translate(parkImage,-100,-100)
cv.imshow("Translated-2",translated2)

translated3 = translate(parkImage,-100,100)
cv.imshow("Translated-3",translated3)

translated4 = translate(parkImage,100,-100)
cv.imshow("Translated-4",translated4)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()