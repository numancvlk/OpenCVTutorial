#ÇİZGİ ÇİZMEK
import cv2 as cv
import numpy as np

blankImg = np.zeros((500,500,3))
cv.imshow("Blank",blankImg)

#ÜSTÜNE ÇİZİLECEK OLAN RESİM, SOL ÜST KÖŞE KOORDİNAT , SAĞ ALT KÖŞE KOORDİNAT, RENK AYARI, KALINLIK
line = cv.line(blankImg, (0,250),(500,250), (0,0,255),thickness=4)
cv.imshow("Line",line)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()