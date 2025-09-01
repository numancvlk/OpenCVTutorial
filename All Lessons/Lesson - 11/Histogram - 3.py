#COLORED HİSTOGRAM MASKESİZ
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",img)
colors = ("b","g","r")

plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

#Renk isimlerini tutuyor (blue, green, red).
#Bu tuple sayesinde matplotlib grafikte hangi rengi çizeceğimizi biliyoruz.
colors = ("b","g","r")

# enumerate hem index (0,1,2), hem de değer ("b","g","r") döndürür.
# Yani döngü şu şekilde çalışıyor:
# tur: i=0, col="b"
# tur: i=1, col="g"
# tur: i=2, col="r"

# Buradaki i → kanal numarası.
# 0 → Mavi kanal
# 1 → Yeşil kanal
# 2 → Kırmızı kanal

for i, col in enumerate(colors):
    normalHist = cv.calcHist([img],[i],None,[256], [0,256])
    plt.plot(normalHist, color= col)
    plt.xlim((0,256))

plt.show()

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()