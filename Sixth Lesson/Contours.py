#KONTÜR BULMAK VE KONTÜRLERİ GÖRSELLEŞTİRMEK SIRA ŞU ŞEKİLDE --> RESMİ GRAY YAP - THRESHOLDUNU BUL veya CANNY ile kenarları bul - KONTÜRLERİ BULUP - KONTÜRLERİ ÇİZ
import cv2 as cv
import numpy as np

cats = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",cats)

blank1 = np.zeros((cats.shape[0],cats.shape[1],3))
cv.imshow("Blank",blank1)

blank2 = np.zeros((cats.shape[0],cats.shape[1],3))
cv.imshow("Blank",blank2)

gray = cv.cvtColor(cats, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

canny = cv.Canny(cats,125,175)
cv.imshow("Canny",canny)

# cv.RETR_LIST → Tüm konturları bulur, ama hiyerarşi ilişkisini kurmaz (yani iç-dış ilişkisi yok, hepsini tek listeye atar).
# cv.RETR_EXTERNAL → Sadece en dıştaki konturları alır (örneğin iç içe daireler varsa sadece en dıştakini alır).
# cv.RETR_TREE → Tüm konturları bulur ve hiyerarşik ilişki kurar (hangi kontur kimin içinde, ebeveyn-çocuk ilişkisi).
# cv.RETR_CCOMP → Konturları iki seviyeye ayırır: dış ve iç.

# cv.CHAIN_APPROX_NONE → Tüm noktaları saklar. (Konturun her pikselini verir. Çok fazla veri olur.)
# cv.CHAIN_APPROX_SIMPLE → Gereksiz noktaları siler. (Örneğin düz çizgide sadece iki uç noktayı saklar, ortadaki 100 noktayı siler.) Daha az veri → daha hızlı.

#-----------------EN SIK KULLANILANLAR---------------------
# cv.RETR_EXTERNAL → sadece dış konturlar lazımsa (örneğin nesne sayma, coin detection gibi). HİERARCHY DEĞİŞKENİ BUNDA GEREKSİZ
# cv.RETR_TREE → iç içe konturlar da önemliyse (örneğin bir şeklin iç boşluklarını da bulmak istiyorsan). HİERARCHY DEĞİŞKENİ BUNDA İŞE YARAR
# cv.CHAIN_APPROX_SIMPLE → %90 durumda bu kullanılır çünkü gereksiz noktalardan kurtarır, daha hafif veri olur.

contours1, _ = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(f"RETR_EXTERNAL = {len(contours1)}")

contours2, hierarchy = cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(f"RETR_TREE = {len(contours2)}")

# 3. parametredeki -1 "contours1" in tüm kontürlerini çiz demek
cv.drawContours(blank1,contours1,-1,(0,0,255),thickness=2)
cv.imshow("Contour - 1", blank1)

cv.drawContours(blank2,contours2,-1,(0,0,255),thickness=2)
cv.imshow("Contour - 2", blank2)


#SİYAH BEYAZ RESİM YAPIYOR EN NİHAYETİNDE
#125'den küçük değerleri siyah, 125'den büyükse beyaz yapar
#MAX_VALUE hep 255 olsun.
#RET = kullanılan threshold değeri (sabit veya otomatik hesaplanmış).
#THRESH = SİYAH BEYAZ RESMİ DÖNER

ret, thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow("THRESHOLD",thresh)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()