#MASKELİ HİSTOGRAM
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",img)

blank = np.zeros((img.shape[0],img.shape[1]),dtype="uint8")

catGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

circleMask = cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),200,255,thickness=-1)

catMask = cv.bitwise_and(catGray,catGray,mask=circleMask)
cv.imshow("MASKED CATS",catMask)

# catGray: gri resim
# [0]    : hangi kanal (grayscale olduğu için 0. kanal)
# catMask: maske resmi (sadece dairenin içi alınacak)
# [256]  : histogramdaki bin sayısı
# [0,256]: değer aralığı (0 siyah, 255 beyaz)
maskedCatsHist = cv.calcHist([catGray],[0],catMask,[256],[0,256]) #MASKEYİ TEK KANALLI VERMEN LAZIM HER ZAMAN YOKSA ÇALIŞMAZ
normalCatsHist = cv.calcHist([catGray],[0],None,[256],[0,256])

print(catMask.shape) #BUDA TEK KANAL
print(circleMask.shape) #BUDA TEK KANAL

plt.figure()
plt.title("GRAY MASKED CAT HISTOGRAM")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.xlim((0,256))
plt.plot(maskedCatsHist)


plt.figure()
plt.title("NORMAL CAT HISTOGRAM")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim((0,256))
plt.plot(normalCatsHist)
plt.show()

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()