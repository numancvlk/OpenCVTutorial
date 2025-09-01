#RESMİN KENARLARINI BULMAK
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park", parkImage)

#Görüntüdeki ani renk/değer değişimlerini (yani kenarları) bulur.
# Bunlar alt eşik ve üst eşik değerleridir:
# 125 = min threshold (lower)
# 200 = max threshold (upper)
# 📌 Algoritmanın mantığı:
# Eğer bir pikselin gradyanı (yani parlaklık değişim gücü) 200’den büyükse, o piksel kesin kenar kabul edilir.
# Eğer gradyan 125’ten küçükse, kesinlikle kenar değil.
# Eğer gradyan 125 ile 200 arasındaysa, bu pikseller “kararsız bölge”ye girer → eğer komşularında güçlü kenar varsa kenara dahil edilir, yoksa atılır.
# Düşük değerler (ör. 50, 100): Çok fazla kenar bulur (gürültü artar).
# Yüksek değerler (ör. 200, 250): Sadece güçlü kenarlar kalır (detaylar kaybolur).

edges = cv.Canny(parkImage,125,200)
cv.imshow("Canny",edges)

key = cv.waitKey(0)

if key ==27:
    cv.destroyAllWindows()