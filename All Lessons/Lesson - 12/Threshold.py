import cv2 as cv

cats = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",cats)

grayCats = cv.cvtColor(cats,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cats",grayCats)

#-----------------------------------------------------------

# cv.threshold(src, thresh, maxval, type):
# src: Girdi resmi (burada grayCats).
# thresh: Eşik değeri (100). Piksel değeri bundan büyükse beyaz, küçükse siyah.
# maxval: Eşiklemeyi geçtiğinde pikselin alacağı değer (255 = beyaz).
# type: Eşikleme türü (cv.THRESH_BINARY = normal binary eşikleme).
# thresh: Eşiklenmiş resim.
# threshold: Fonksiyonun döndürdüğü eşik değeri (burada direkt verdiğimiz için 100).

#SIMPLE THRESHOLDING
threshold, thresh = cv.threshold(grayCats,100,255,cv.THRESH_BINARY)
cv.imshow("Simple Threshold",thresh)

#-----------------------------------------------------------

# cv.THRESH_BINARY_INV: Ters eşikleme.
# Piksel değeri eşik değerinden büyükse siyah (0),
# Küçükse beyaz (255) yapılır.

#SIMPLE THRESHOLDING INVERSE
threshold, threshInv = cv.threshold(grayCats,100,255,cv.THRESH_BINARY_INV)
cv.imshow("Threshold Inverse",threshInv)

#-----------------------------------------------------------

# Farkı ne? Simple threshold global (tüm resim için aynı eşik), adaptif threshold her piksel için çevresine bakarak farklı eşik değeri belirler. 
# Yani ışık farkı olan resimlerde daha iyi çalışır.
# Parametreler:
# grayCats: Gri resim
# 255: Maksimum değer (beyaz)
# cv.ADAPTIVE_THRESH_MEAN_C: Eşikleme yöntemi, çevresindeki piksellerin ortalamasına göre eşik belirler.
# cv.THRESH_BINARY: Binary eşikleme
# 11: Blok boyutu (çevredeki kaç piksele bakılacak)
# 5: C değeri, eşik değerinden çıkarılacak sabit. Yani Eşik = Ortalama - C

#ADAPTIVE THRESHOLDING WITH MEAN
adaptiveThreshold = cv.adaptiveThreshold(grayCats,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,5)
cv.imshow("Adaptive Threshold",adaptiveThreshold)

#-----------------------------------------------------------

# Ters adaptif eşikleme. Piksel değeri eşikten büyükse siyah, küçükse beyaz yapılır.

#ADAPTIVE THRESHOLDING INVERSE WITH MEAN
adaptiveThresholdInverse = cv.adaptiveThreshold(grayCats,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,5)
cv.imshow("Adaptive Threshold Inverse",adaptiveThresholdInverse)

#-----------------------------------------------------------

# cv.ADAPTIVE_THRESH_GAUSSIAN_C:
# Pikselin eşik değeri, çevresindeki piksellerin ortalamasının ağırlıklı (gauss) ortalaması alınarak belirlenir.

#ADAPTIVE THRESHOLDING WITH GAUSSIAN
adaptiveThresholdG = cv.adaptiveThreshold(grayCats,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)
cv.imshow("Adaptive Threshold WITH GAUSSIAN",adaptiveThresholdG)

#-----------------------------------------------------------

#ADAPTIVE THRESHOLDING INVERSE WITH GAUSSIAN
adaptiveThresholdInverseG = cv.adaptiveThreshold(grayCats,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,5)
cv.imshow("Adaptive Threshold WITH GAUSSIAN INVERSE",adaptiveThresholdInverseG)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()