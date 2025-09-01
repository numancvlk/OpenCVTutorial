#RESMİN RENKLERİNİ GRI YAPMAK
import cv2 as cv

catImage = cv.imread("Photos\cat.jpg")
cv.imshow("Cat Original",catImage)

grayCat = cv.cvtColor(catImage,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY CAT", grayCat)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()