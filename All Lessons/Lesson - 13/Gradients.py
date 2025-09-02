#EDGE DETECTION

import cv2 as cv
import numpy as np

park = cv.imread("Photos\cats.jpg")
gray = cv.cvtColor(park,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY PARK",gray)

#Laplacian = Hem dikey hem yatay değişimleri tek seferde yakalayabilir. 2. TÜREV İLE KENARLARI YAKALAR
# cv.Laplacian(src, ddepth):
# src: Gri resim (gray)
# ddepth: Çıktı veri tipi (cv.CV_64F)
# Kenar değerleri negatif olabileceği için float64 kullanılır.

lap = cv.Laplacian(gray,cv.CV_64F)

# np.absolute(lap): Laplacian sonucu negatif değerler olabilir, mutlak değer alıyoruz.
# np.uint8(...): OpenCV görüntüleme için 0-255 aralığına çeviriyoruz.
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#SOBEL = Kenar yönünü seçebilirsin, daha pürüzsüz kenar 1. TÜREV İLE KENARLARI YAKALAR
# cv.Sobel(src, ddepth, dx, dy):
# src: Gri resim
# ddepth: Çıktı veri tipi (cv.CV_64F)
# dx: X yönünde türev alınacak mı? (1 = evet, 0 = hayır)
# dy: Y yönünde türev alınacak mı? (1 = evet, 0 = hayır)

# xSobel: Yalnızca yatay kenarlar (dikey değişimleri gösterir)
xSobel = cv.Sobel(gray,cv.CV_64F,1,0)

# ySobel: Yalnızca dikey kenarlar (yatay değişimleri gösterir)
ySobel = cv.Sobel(gray,cv.CV_64F,0,1)

# combinedSobel: bitwise_or ile hem yatay hem dikey kenarları birleştiriyoruz.
combinedSobel = cv.bitwise_or(xSobel,ySobel)

cv.imshow("X SOBEL", xSobel)
cv.imshow("Y SOBEL",ySobel)
cv.imshow("Combined Sobel",combinedSobel)


key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()