#COLORED HISTOGRAM MASKELİ
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos\cats.jpg")

blank = np.zeros((img.shape[:2]),dtype="uint8")

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,thickness=-1)
cv.imshow("Circle",circle)

# Eğer circleMask olarak bitwise_and yaparsak, 3 kanallı renkli resim oluşur
# cv.calcHist fonksiyonu 3 kanallı görüntü ile maskeyi kullanamaz
# Bu yüzden histogram için doğrudan tek kanallı maskeyi kullanıyoruz: circle
circleMask = cv.bitwise_and(img,img,mask=circle)

print(circleMask.shape) #3 KANALLI RESİM OLDUĞU İÇİN HİSTOGRAMA VEREMİYORSUN YA RESMİ GRİ YAPCAKSIN AMA BURDA OLMAZ RENKLİ HİSTOGRAM ALIYORUZ
# YADA GİDİP BLANK OLUŞTURCAKSIN TEK KANAL OLUYOR ZATEN OZAMAN CİRCLE ÇİZCEN İÇNİE FALAN

print(circle.shape) # BU İSE TEK KANALLI 3. PARAMETRE KANAL SAYISINI GÖSTERİYOR YOKSA TEK KANALLIDIR.

plt.figure()
plt.title("COLORED HISTOGRAM MASKELİ")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
colors = ("b","g","r")

for i, col in enumerate(colors):
    coloredHistMasked = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(coloredHistMasked, color= col)
    plt.xlim((0,256))

plt.show()

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()