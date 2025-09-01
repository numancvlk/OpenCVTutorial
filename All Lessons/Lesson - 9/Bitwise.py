#BITWISE
import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype="uint8")

rectangle = cv.rectangle(blank.copy(),(50,50),(450,450),255,thickness=-1)
circle = cv.circle(blank.copy(),(250,250),250,255,thickness=-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#BITWISE AND = YALNIZCA İKİ ŞEKİLDEKİ ORTAK PİKSELLERİ ALIR
bitwise_AND = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise AND",bitwise_AND)

#BITWISE OR = KESİŞEN VE KESİŞMEYEN TÜM PİKSELLERİ ALIR
bitwise_OR = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR",bitwise_OR)

#BITWISE XOR = YANLIZCA KESİŞMEYEN PİKSELLERİ ALIR
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR",bitwise_XOR)

#BITWISE NOT = Tek parametre alır. Circle verdik mesela circle hariç her yeri beyaz yapar.
bitwise_NOT = cv.bitwise_not(circle)
cv.imshow("Circle NOT",bitwise_NOT)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()