#DAİRE ÇİZMEK
import cv2 as cv
import numpy as np

blankImg = np.zeros((500,500,3))
cv.imshow("Blank",blankImg)

#BURADA VERDİĞİN KOORDİNATLAR DAİRENİN ORTASINI TEMSİL EDER YANİ DAİRENİN MERKEZİ O KOORDİNATLAR OLUR.
#ÜSTÜNE ÇİZİLECEK RESİM, DAİRENİN HANGİ KOORDİNATLARA ÇİZİLECEĞİ (BURADA RESMİN ORTASI), DAİRENİN YARIÇAPI, DAİRENİN RENGİ, KALINLIK
circle_1 = cv.circle(blankImg, (blankImg.shape[1] // 2, blankImg.shape[0] // 2), 100, (0,0,255),thickness=5)
cv.imshow("Circle-1", circle_1)

circle_2 = cv.circle(blankImg,(250,220), 100, (255,0,0),thickness=2)
cv.imshow("Circle-2", circle_2)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()