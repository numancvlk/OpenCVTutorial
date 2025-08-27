#RESMİ FLIPLEMEK
import cv2 as cv

groupImage = cv.imread("Photos\group 1.jpg")
cv.imshow("Group",groupImage)

flippedVertical = cv.flip(groupImage,0) # 0 --> Y ekseninde takla attırır
cv.imshow("Vertical Flip",flippedVertical)

flippedHorizontal = cv.flip(groupImage,1) # 1 --> X ekseninde takla atttırır (AYNA)
cv.imshow("Horizontal Flip",flippedHorizontal)

flippedVerticalAndHorizontal = cv.flip(groupImage,-1)
cv.imshow("Vertical and Horizontal Flip",flippedVerticalAndHorizontal) # -1 --> Hem Y ekseninde hem de X eksenin resme takla attırır

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()