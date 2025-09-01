#CANNY İLE KENARLARI BULDUKTAN SONRA KENARLARI DILATE İLE KALINLAŞTIRIP ERODE İLE İNCELTMEK
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("PARK",parkImage)

#RESMİN KENARLARINI BULDU
canny = cv.Canny(parkImage,125,200) 
cv.imshow("CANNY",canny)

#KENARLARI BULUNAN RESMİN BEYAZ OLAN KISIMLARINI KALINLAŞTIRDI
dilated = cv.dilate(canny,(7,7),iterations=1) 
cv.imshow("DILATED",dilated)

#BEYAZ KISIMLARI KALINLAŞAN RESMİN BEYAZ KISIMLARINI İNCELTTİ VE küçük beyaz noktaları yok eder → yani gürültü temizliği yapar.
#2. PARAMETRE YANİ KERNEL BÜYÜK SEÇERSEN DAHA ÇOK AŞINIR KENARLAR YOK OLABİLİR DAHA KÜÇÜK SEÇERSEN DAHA AZ AŞINIR KENARLAR İNCELİR
eroded = cv.erode(dilated,(7,7),iterations=1) 
cv.imshow("ERODED",eroded)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()