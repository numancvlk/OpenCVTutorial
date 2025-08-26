#CANNY İLE GELEN İNCE KENARLARI KALINLAŞTIRMAK
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

#ŞİMDİ ÖNCE CANNY İLE KENARLARI BULUYORSUN YİNE
canny = cv.Canny(parkImage,125,200)
cv.imshow("Canny", canny)

#SONRA BU cv.dilate ile o ince olan kenarları kalınlaştırıyorsun.
# 1. PARAMETRE RESİM, 2.PARAMETRE NE KADAR KALINLAŞSIN, 3.PARAMETRE KAÇ KERE KALINLAŞTIRMA İŞLEMİNİ YAPSIN
#2. PARAMETRE YANİ KERNELİ BÜYÜK SEÇERSEN O KADAR ÇOK KALINLAŞIR KÜÇÜK SEÇERSEN AZ KALINLAŞIR
dilated = cv.dilate(canny,(7,7),iterations=1)
cv.imshow("Dilated Park",dilated)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()