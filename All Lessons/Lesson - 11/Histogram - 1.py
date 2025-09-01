#MASKESİZ HİSTOGRAM
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#[gray] → hangi görüntüden histogram alacağımız.
#[0] → hangi kanaldan (0 = grayscale).
#None → maske kullanılmıyor (tüm görüntü dahil).
#[256] → 256 kutu (bin) var, yani 0–255 arasındaki değerler ayrı ayrı sayılıyor.
#[0,256] → piksel aralığı.

grayHist = cv.calcHist([gray],[0],None,[256],[0,256]) 

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim((0,256))
plt.plot(grayHist)
plt.show()

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()