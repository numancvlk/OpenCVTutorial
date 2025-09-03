#EĞİTTİĞİMİZ DATAYI BURDA KULLANCAZ
import cv2 as cv
import numpy as np

people =  ["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"]

haarCascade = cv.CascadeClassifier("haarFace.xml")

# features = np.load("features.npy")
# labels = np.load("labels.npy")

faceRecognizer = cv.face.LBPHFaceRecognizer.create()
faceRecognizer.read("faceTrained.yml")

img = cv.imread("Faces\Train\Ben Afflek\1.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person",gray)

facesRect = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,width,height) in facesRect:
    facesRoi = gray[y:y+height,x:x+width]

    label, confidence = faceRecognizer.predict(facesRoi)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv.putText(img,str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+width,y+height),(0,255,0),thickness=2)

cv.imshow("Detected Face",img)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()