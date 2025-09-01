#COLOR SPACES = RENKLERİ KANALLARA AYIRMAK
import cv2 as cv
import numpy as np

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

blankImage = np.zeros((parkImage.shape[:2]),dtype="uint8")

#RESMİ BLUE, GREEN, RED ŞEKLİNDE KANALLARA AYIRDIK RESİMLER GRİ ÇIKIYOR.
# Blue, Green, Red kanallarının yoğunluklarını ayrı ayrı görmemizi sağlar
#Örneğin, bir bölgede sadece gökyüzü maviyse, blue kanalında orası çok açık çıkacak, ama red kanalında koyu görünecek.

blue, green, red = cv.split(parkImage)
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

#cv.merge() ise tüm renk kanallarını bir araya getirip orijinal resmi tekrardan çıkarıyoruz.

mergedImage = cv.merge((blue,green,red))
cv.imshow("Merged Image",mergedImage)


#EĞER YUKARIDAKİ GİBİ GRİ OLARAK GÖRMEK İSTEMEZSEN RENK KANALLARINI BU ŞEKİLDE RENKLİ GÖREBİLİRSİN.
blueImg = cv.merge((blue,blankImage,blankImage))
greenImg = cv.merge((blankImage,green,blankImage))
redImg = cv.merge((blankImage,blankImage,red))

cv.imshow("Colored Blue",blueImg)
cv.imshow("Colored Green",greenImg)
cv.imshow("Colored Red",redImg)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()