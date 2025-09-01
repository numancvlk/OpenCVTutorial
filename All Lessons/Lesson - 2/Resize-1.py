#RESİMLERİ YENİDEN ÖLÇEKLENDİRME
import cv2 as cv

#BU METHOD SADECE IMAGE, VIDEO ve Live Video'da çalışıyor.
def rescaleFrame(frame,scale = 0.75): #RESMİ YENİDEN ÖLÇEKLENDİRMEK İÇİN FONSKİYONUMUZ SCALE DEFAULT OALRAK 0.75 OLSUN HEP
    height = int(frame.shape[0] * scale) #FRAME.shape[0] resmin HEIGHT değerini temsil eder.
    width = int(frame.shape[1] * scale) #FRAME.shape[1] resmin WIDTH değerini temsil eder.
    dimension = (width,height) #BU TUPLE TİPLİ DEĞİŞKEN
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA) #cv.resize 1. değeri frame 2. değeri dimension 3. değeri ise küçülttüğümüz için INTER_AREA en iyisi

img = cv.imread("Photos\cat_large.jpg")

imgResized = rescaleFrame(img,0.20)

cv.imshow("CAT ORIGINAL", img)
cv.imshow("CAT RESIZED", imgResized)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()