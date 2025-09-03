import os
import cv2 as cv
import numpy as np

people =  ["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"]

DIRECTION = "Faces\Train"

haarCascade = cv.CascadeClassifier("haarFace.xml")

features = []
labels = []

def createTrain():
    for person in people:
        path = os.path.join(DIRECTION,person)
        label = people.index(person)

        for img in os.listdir(path):
            imgPath = os.path.join(path,img)
            
            imgArray = cv.imread(imgPath)
            gray = cv.cvtColor(imgArray,cv.COLOR_BGR2GRAY)

            facesRectangle = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,width,height) in facesRectangle:
                facesRoi = gray[y:y+height,x:x+width]
                features.append(facesRoi)
                labels.append(label)
                # cv.rectangle(imgArray,(x,y),(x+width,y+height),(0,255,0),thickness=2)

createTrain()

print("-----------------TRAINING DONE-----------------")

features = np.array(features,dtype="object")
labels = np.array(labels)

faceRecognizer = cv.face.LBPHFaceRecognizer.create()
faceRecognizer.train(features,labels)

faceRecognizer.save("faceTrained.yml")
np.save("features.npy",features)
np.save("labels.npy",labels)