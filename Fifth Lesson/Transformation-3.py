#RESMİN BOYUTUNU BÜYÜLTMEK
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

resized = cv.resize(parkImage,(1000,1000),interpolation=cv.INTER_CUBIC) #CUBIC KULLANMA SEBEBİMİZ RESMİN DAHA KALİTELİ OLAMSINI SAĞLAMAK
cv.imshow("Resized Park",resized)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()