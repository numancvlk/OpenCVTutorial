#FACE DETECT
import cv2 as cv

img = cv.imread("Photos\lady.jpg")
cv.imshow("Person",img)

grayPerson = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Person",grayPerson)

# Haar cascade, OpenCV'nin önceden eğitilmiş bir yüz tespit modelidir. XML dosyası bu modelin parametrelerini içerir.
haarCascade = cv.CascadeClassifier("haarFace.xml") #XML DOSYASINI OKU VE DEĞİŞKENE AT

# detectMultiScale() fonksiyonu resmi farklı boyutlarda tarayarak yüzleri arar.
# Parametreler:
# grayPerson -> üzerinde yüz arayacağımız gri resim
# scaleFactor=1.1 -> her adımda pencerenin boyutunu ne kadar küçülteceğini belirler. 1.1 yerine 1.05 kullanırsan daha hassas tarar (daha çok pencere), 1.3 kullanırsan daha hızlı ama daha az hassas olur. HER ZAMAN 1'DEN BÜYÜK OLMALI!
# minNeighbors=3 -> bir yüz adayı kabul edilebilmesi için çevresinde en az 3 komşu dikdörtgen olmalı. DEĞERİ HER ZMAAN 1'DEN BÜYÜK OLMALI!!
# Fonksiyon, bulunan yüzlerin koordinatlarını (x, y, width, height) olarak döndürür.
faceRectangle = haarCascade.detectMultiScale(grayPerson,scaleFactor=1.1,minNeighbors=3)

# Bulunan yüz sayısını ekrana yazdırıyoruz.
print(f"Number of faces = {len(faceRectangle)}") #KAÇ TANE YÜZ BULDUĞUNU BİZE DÖNER

# Her bulunan yüz için bir dikdörtgen çiziyoruz.
# faceRectangle bir liste şeklindedir ve her öğesi (x, y, width, height) koordinatlarını içerir.
for (x,y,width,height) in faceRectangle:
    # cv.rectangle ile resim üzerinde dikdörtgen çiziyoruz
    # (x, y) -> dikdörtgenin sol üst köşesi
    # (x+width, y+height) -> dikdörtgenin sağ alt köşesi
    cv.rectangle(img,(x,y),(x+width,y+height),(0,255,0),thickness=2)

# Yüzleri dikdörtgenlerle işaretlenmiş resmi gösteriyoruz.
cv.imshow("Detected Faces",img)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()