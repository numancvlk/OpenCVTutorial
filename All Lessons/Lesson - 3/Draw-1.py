#SLICING İLE ŞEKİL ÇİZMEK VE RENKLERLE OYNAMAK
import cv2 as cv
import numpy as np

blackImg = np.zeros((500,500,3)) #0'lar siyah 200px height 200px width 3 ise BGR (BLUE,GREEN,RED) şeklinde 1 yazsaydık oraya resim siyah beyaz olurdu.
cv.imshow("Blank",blackImg)

whiteImg = np.ones((200,200,3)) #1'ler beyaz
cv.imshow("Ones",whiteImg)

blackImg[:] = (255,0,0) #PİKSELLERİN HEPSİNİ SEÇİYORUZ
cv.imshow("Blue", blackImg)

blackImg[:] = (0,0,255) #PİKSELLERİN HEPSİNİ SEÇİYORUZ
cv.imshow("Red",blackImg)

blackImg[:] = (0, 255, 0) #PİKSELLERİN HEPSİNİ SEÇİYORUZ
cv.imshow("Green",blackImg)

blackImg[150:200, 150:200] = (0,0,255) #50X50lik bir kutu yaptık çünkü 200-150 = 50
cv.imshow("Draw-1",blackImg) #OPENCVde (0,0) noktası sol üst köşedir! blackImg[y cor, x cor] şeklinde yazılır! 

whiteImg[100:110,0:200] = (255,0,0) #BEYAZ RESMİN ÜZERİNE MAVİ BİR ÇİZGİ ÇEKTİK BU SAYEDE
cv.imshow("Draw-2", whiteImg)

img = cv.imread("Photos\cat.jpg")
cv.imshow("Cat",img)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()