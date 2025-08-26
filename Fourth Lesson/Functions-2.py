#RESİM BULANIKLAŞTIRMA
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

#HANGİ RESMİ BULANIKLAŞTIRACAĞIN, (X,Y)'DE BULANIKLIĞIN KAÇA KAÇ OLSUN, BURDA DİREKT cv.BORDER_DEFAULT kullan daha iyi
#(ÇOK ÖNEMLİ!! BURDAKİ (x,y) SAYILARI HER ZAMAN TEK SAYI OLMALI)
blur1 = cv.GaussianBlur(parkImage,(7,15),cv.BORDER_DEFAULT)
cv.imshow("BLUR-1",blur1)

blur2 = cv.GaussianBlur(parkImage,(1,9),cv.BORDER_CONSTANT) #EĞER RESMİNİN KENARLARI SIKINTILI İSE BUNU KULLAN KENARLARI SİYAH YAPAR
cv.imshow("BLUR-2",blur2)


key = cv.waitKey(0)

if key ==27:
    cv.destroyAllWindows()