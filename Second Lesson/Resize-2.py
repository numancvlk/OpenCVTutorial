#VİDEOLARI YENİDEN ÖLÇEKLENDİRME
import cv2 as cv

#BU METHOD SADECE IMAGE, VIDEO ve Live Video'da çalışıyor.
def rescaleFrame(frame,scale= 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = (height,width)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("Videos\dog.mp4")

while True:
    isTrue, frame = capture.read()
    resizedCapture = rescaleFrame(frame,0.2)

    if isTrue:
        cv.imshow("Dog Original",frame)
        cv.imshow("Dog Resized",resizedCapture)
    else:
        print("Frame doesn't exist")
        break

    key = cv.waitKey(20)
    if key == 27:
        cv.destroyAllWindows()
        break

capture.release()
cv.destroyAllWindows()
