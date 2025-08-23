#RESMİN İÇERSİNE YAZI KOYMAK
import cv2 as cv 
import numpy as np

blankImg = np.zeros((500,500,3))
cv.imshow("Blank", blankImg)

#Bu fonksiyona özel durum verdiğimiz koordinatlar yazımızın sol alt köşesini temsil ediyor. Yani yazı oradan başlıyor.
#ÜSTÜNE YAZI YAZMAK İSTEDİĞİN RESİM, STRİNGİN, KOORDİNATLARIN, FONT TİPİN, SCALE 1.0 İYİ, COLOR, KALINLIK
text = cv.putText(blankImg,"Hello OpenCV", (150, blankImg.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow("Text",text)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()