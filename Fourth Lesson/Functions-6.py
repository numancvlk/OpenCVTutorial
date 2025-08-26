#RESMİ RESIZE ETME
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

#1. PARAMETRE RESİM, 2. PARAMETRE DİREK BOYUTLAR (WIDTH, HEIGHT)PX, 3. PARAMETRE DAHA AZ MOZAİKLENME İÇİN cv.INTER_AREA
#BİZİM RESIZE FONKSİYONU DAHA İYİ AMA BUDA AKLINDA KALSIN
resized = cv.resize(parkImage,(300,500),interpolation=cv.INTER_AREA)
cv.imshow("Resized Park", resized)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()