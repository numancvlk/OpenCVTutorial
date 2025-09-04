#YÜZLERİ ALGILAMAK İÇNİ BURDA MODELİ EĞTİİYROUZ
import os
import cv2 as cv
import numpy as np

# Tanıyacağımız kişilerin isimleri ASLINDA DOSYALARIN İSİMLERİ DAHA KOALY YOLUDA VAR ÇOK KİŞİ VARSA
people =  ["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"]

# Eğitim resimlerinin bulunduğu klasör yolu
DIRECTION = "C:\\OPENCV\\OpenCVTutorial\\Faces\\Train"

# Yüzleri algılamak için Haar Cascade dosyasını yüklüyoruz
haarCascade = cv.CascadeClassifier("haarFace.xml")

# Eğitimde kullanılacak veriler
features = [] # Yüzün ROI (Region of Interest → yüz kısmı)
labels = [] # O ROI’ye karşılık gelen etiket (hangi kişi olduğunu gösteriyor)

def createTrain():
    for person in people: # listedeki her kişi için
        path = os.path.join(DIRECTION,person) # kişinin resimlerinin olduğu klasör
        label = people.index(person)  # kişinin index numarası (etiket)

        for img in os.listdir(path): # Klasördeki her resim için
            imgPath = os.path.join(path,img) # resmin tam yolu
            
            # Resmi okuma
            imgArray = cv.imread(imgPath) 
            gray = cv.cvtColor(imgArray,cv.COLOR_BGR2GRAY)


            faces = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4) # Resimde yüz tespiti yapma

            for (x,y,width,height) in faces: # Tespit edilen her yüz için ROI çıkar
                facesRoi = gray[y:y+height,x:x+width] # resmin sadece ilgili yüz kısmını kesip almak
                features.append(facesRoi) # yüz verilerini ekle
                labels.append(label)  # o yüzün hangi kişiye ait olduğunu kaydet

createTrain()

print("-----------------TRAINING DONE-----------------")

# Verileri numpy array formatına çevir
features = np.array(features,dtype="object")
labels = np.array(labels)

# LBPH (Local Binary Patterns Histograms) yüz tanıma algoritmasını kullan
faceRecognizer = cv.face.LBPHFaceRecognizer.create() #ÖNCE CREATE ETMEN LAZIM!
faceRecognizer.train(features,labels) # Verilerle modeli eğit

faceRecognizer.save("faceTrained.yml") # Eğitilmiş modeli kaydet

# Eğitimde kullanılan verileri kaydet (ileride lazım olabilir)
np.save("features.npy",features)
np.save("labels.npy",labels)