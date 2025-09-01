#RESİM OKUMA VE GÖSTERME
import cv2 as cv #OPENCV

img = cv.imread("Photos\cat.jpg") #YOLUNU VERDİĞİMİZ RESMİ MATRİX OLARAK OKUR

cv.imshow("Cat",img) #1. Pencerenin ismi 2. Görüntülenecek resmimiz

key = cv.waitKey(0) #Bunu kullanmazsan resim ekrana gelip gider parametresi milisaniye console.readline() gibi

if key == 27: #27 = ESC tuşu
    cv.destroyAllWindows() #Tüm açılan sekmeleri kapatmak için kullanılır.