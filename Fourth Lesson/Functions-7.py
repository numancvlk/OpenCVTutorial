#RESMİ CROPLAMA
import cv2 as cv

parkImage = cv.imread("Photos\park.jpg")
cv.imshow("Park",parkImage)

#[y1:y2, x1:x2] bu şekilde yapıyorsun slicing olayını önce y ekseni start stop
# sonra x ekseni start stop
cropped = parkImage[50:200,400:600]
cv.imshow("Cropped Park", cropped)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()