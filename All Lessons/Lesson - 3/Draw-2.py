#DİKDÖRTGEN ÇİZMEK
import cv2 as cv
import numpy as np

blackImg = np.zeros((500,500,3))
cv.imshow("Blank", blackImg)

#pt1 → Dikdörtgenin sol üst köşe koordinatı (x1, y1)

#pt2 → Dikdörtgenin sağ alt köşe koordinatı (x2, y2)
rectangle_1 = cv.rectangle(blackImg, (0,0),(250,270), (0,255,0), thickness=cv.FILLED) #ÜSTÜNE ÇİZİM YAPACAĞIN RESİM, SOL ÜST KÖŞE KOORDİNATLARI, SAĞ ALT KÖŞE KOORDİNATLARI, KALINLIK(FİLLED YAZARSAN İÇİNİ DOLDURUR)
cv.imshow("Rectangle-1",rectangle_1)

rectangle_2 = cv.rectangle(blackImg,(200,200),(300,400),(255,0,0),thickness=4)
cv.imshow("Rectangle-2",rectangle_2)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()