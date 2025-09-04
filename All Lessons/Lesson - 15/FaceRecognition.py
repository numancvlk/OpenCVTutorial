#EĞİTTİĞİMİZ DATAYI BURDA KULLANCAZ
import cv2 as cv
import numpy as np

people =  ["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"] #İNSANLARIN İSİMLERİ

haarCascade = cv.CascadeClassifier("haarFace.xml") #YÜZ ALGILAMA MODELİMİZ AMA HAZIR OLAN

# features = np.load("features.npy")
# labels = np.load("labels.npy")

faceRecognizer = cv.face.LBPHFaceRecognizer.create() #LBPH (Local Binary Patterns Histograms) yüz tanıma modeli oluşturuluyor.
faceRecognizer.read("faceTrained.yml") #Daha önce kaydettiğimiz faceTrained.yml dosyasından eğitilmiş ağırlıklar yükleniyor.

#VALIDATION İÇİN KULLANACAĞIMIZ RESMİ YÜKLEYİP GRİYE ÇEVİRİYORUZ
img = cv.imread(r"C:\\OPENCV\\OpenCVTutorial\\Faces\\Val\\elton_john\\2.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person",gray)

facesRect = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4) #HAZIR YÜZ ALGILAMA MODELİ İLE YÜZÜ YAKALIYORUZ

for (x,y,width,height) in facesRect:
    facesRoi = gray[y:y+height,x:x+width] # Verilen resim ile ilgili region of interest çıkarılıyor

    #label = hangi kişiye ait olduğunu söylüyor (index).
    #confidence = güven değeri. (Küçük değer = daha güvenilir tanıma).
    label, confidence = faceRecognizer.predict(facesRoi) #model tahmin yapıyor
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv.putText(img,str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+width,y+height),(0,255,0),thickness=2)

cv.imshow("Detected Face",img)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()