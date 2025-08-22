#RESİM OKUMA VE GÖSTERME
import cv2 as cv

img = cv.imread("Photos\cat_large.jpg")

cv.imshow("Large Cat" , img)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()