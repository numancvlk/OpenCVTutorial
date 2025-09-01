#MASKING
import cv2 as cv
import numpy as np

img = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",img)

blank = np.zeros((img.shape[:2]),dtype="uint8") #BLANK IMAGE YANİ MASKELEMEYİ YAPACAĞIN YER MASKE ŞEKLİNİN OLACAĞI YER RESİM İLE AYNI BOYUTTA OLMAK ZORUNDA!!

circleMask = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,thickness=-1)
cv.imshow("Circle Mask",circleMask)

rectangleMask = cv.rectangle(blank.copy(),(200,200),(400,400),255,thickness=-1)
cv.imshow("Rectangle Mask",rectangleMask)

masked1 = cv.bitwise_and(img,img,mask=circleMask)
cv.imshow("Masked - 1",masked1)

masked2 = cv.bitwise_and(img,img,mask=rectangleMask)
cv.imshow("Masked - 2",masked2)


key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()