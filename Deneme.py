import cv2 as cv
import numpy as np

#RESMİ BOYUTLANDIRMA
# def rescaleFrame(frame,scale= 0.75):
#     width = int(frame.shape[0] * scale)
#     height = int(frame.shape[1] * scale)
#     dimension = (width,height)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


# largeCat = cv.imread("Photos\cat_large.jpg")
# resizedLargeCat = rescaleFrame(largeCat,0.25) 

# cv.imshow("Large Cat - 1", largeCat)
# cv.imshow("Large Cat - 2", resizedLargeCat)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

#VİDEO BOYUTLANDIRMA
# def resizeFrame(frame,scale=0.75):
#     width = int(frame.shape[0] * scale)
#     height = int(frame.shape[1] * scale)
#     dimension = (width,height)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# dogVideo = cv.VideoCapture("Videos\dog.mp4")

# while True:
#     isTrue, frame = dogVideo.read()
#     dogVideoResized = resizeFrame(frame,0.25)

#     if isTrue:
#         cv.imshow("Dog Video - 1", frame)
#         cv.imshow("Dog Video - 2",dogVideoResized)
#     else:
#         print("Video Bitti")
#         break
    
#     key = cv.waitKey(20)

#     if key == 27:
#         break

# dogVideo.release()
# cv.destroyAllWindows()

#--------------------------------------------------------------------------

#ÇİZGİ ÇİZMEK (METHODSUZ)
# blankImg = np.zeros((500,500,3))
# cv.imshow("Blank Img", blankImg)

# blankImg[240:250,0:500] = (0,0,255)
# cv.imshow("Draw - 1",blankImg)

# blankImg[240:250, 240:280] = (255,0,0)
# cv.imshow("Draw - 2", blankImg)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

#KARE YAPMAK
# blankImg = np.ones((500,1000,3))
# cv.imshow("Blank Image",blankImg)

# cv.rectangle(blankImg,(220,190),(720,250),(255,0,0),thickness=cv.INTER_AREA)
# cv.imshow("Rectangle - 1",blankImg)

# cv.rectangle(blankImg,(230,200),(710,240),(0,255,0),thickness=cv.INTER_AREA)
# cv.imshow("Rectangle - 2", blankImg)

# cv.rectangle(blankImg,(240,210),(700,230),(0,0,255),thickness=cv.INTER_AREA)
# cv.imshow("Rectangle - 3",blankImg)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

#DAİRE ÇİZMEK
# blankImg = np.ones((500,500,3))
# cv.imshow("Blank Image",blankImg)

# cv.circle(blankImg,(250,250),70,(0,0,255),thickness=2)
# cv.imshow("Circle - 1",blankImg)

# cv.circle(blankImg,(250,250),50,(0,255,0),thickness=2)
# cv.imshow("Circle - 2",blankImg)

# cv.circle(blankImg,(250,250),30,(255,0,0),thickness=2)
# cv.imshow("Circle - 3", blankImg)

# cv.circle(blankImg,(250,250),10,(0,0,255),thickness=cv.FILLED)
# cv.imshow("Circle - 4", blankImg)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

#ÇİZGİ ÇİZMEK

# blankImage = np.ones((500,1000,3))
# cv.imshow("Blank Image",blankImage)

# cv.line(blankImage,(450,300),(500,200),(255,0,0),thickness=2)
# cv.imshow("Line - 1",blankImage)

# cv.line(blankImage,(500,200),(550,300),(0,255,0), thickness=2)
# cv.imshow("Line - 2",blankImage)

# cv.line(blankImage,(450,300),(550,300),(0,0,255),thickness=2)
# cv.imshow("Line - 3",blankImage)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows

#--------------------------------------------------------------------------

# blankImage = np.ones((500,1000,3))
# cv.imshow("Blank Image", blankImage)

# cv.putText(blankImage,"MINA",(450,(blankImage.shape[0]//2) - 100),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255))
# cv.imshow("Text - 1", blankImage)

# cv.putText(blankImage,"SENI",(450,(blankImage.shape[0]//2) - 50), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255))
# cv.imshow("Line - 2", blankImage)

# cv.putText(blankImage,"COK",(455,(blankImage.shape[0]//2)),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255))
# cv.imshow("Line - 3",blankImage)

# cv.putText(blankImage,"SEVIYORUM",(400,(blankImage.shape[0]//2) + 50),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255))
# cv.imshow("Line - 4", blankImage)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# parkImage = cv.imread("Photos\park.jpg")
# cv.imshow("Park",parkImage)

# gray = cv.cvtColor(parkImage,cv.COLOR_BGR2GRAY) #RESMI SİYAH BEYAZ YAPTI
# cv.imshow("GRAY",gray)

# hsv = cv.cvtColor(parkImage,cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# hls = cv.cvtColor(parkImage,cv.COLOR_BGR2HLS)
# cv.imshow("HLS",hls)

# lab = cv.cvtColor(parkImage, cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)

# luv = cv.cvtColor(parkImage,cv.COLOR_BGR2LUV)
# cv.imshow("LUV",luv)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# groupImage = cv.imread("Photos\group 1.jpg")
# cv.imshow("Group",groupImage)

# blur1 = cv.GaussianBlur(groupImage,(11,11),cv.BORDER_DEFAULT)
# cv.imshow("BLUR - 1", blur1)

# blurHorizontal = cv.GaussianBlur(groupImage,(19,1),cv.BORDER_DEFAULT)
# cv.imshow("BLUR HORIZONTAL", blurHorizontal)

# blurVertical = cv.GaussianBlur(groupImage,(1,19),cv.BORDER_DEFAULT)
# cv.imshow("BLUR VERTICAL", blurVertical)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# groupImage = cv.imread("Photos\group 2.jpg")
# cv.imshow("Group",groupImage)

# cannyLess = cv.Canny(groupImage,50,100)
# cv.imshow("CANNY LESS THRESHOLD",cannyLess)

# cannyMore = cv.Canny(groupImage,150,250)
# cv.imshow("CANNY MORE THRESHOLD",cannyMore)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# groupImage = cv.imread("Photos\group 1.jpg")
# cv.imshow("Group", groupImage)

# canny = cv.Canny(groupImage,50,100)
# cv.imshow("CANNY", canny)

# dilatedLess = cv.dilate(canny,np.ones((2,2)),iterations=1) ##KERNEL VERİRKEN np.ones() ile ver yoksa çalışmıyor.
# cv.imshow("LESS DILATE",dilatedLess)

# dilatedMore = cv.dilate(canny, np.ones((7,7)),iterations=1) ##KERNEL VERİRKEN np.ones() ile ver yoksa çalışmıyor.
# cv.imshow("MORE DILATE", dilatedMore)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# groupImage = cv.imread("Photos\group 1.jpg")
# cv.imshow("Group",groupImage)

# canny = cv.Canny(groupImage,200,300)
# cv.imshow("Canny",groupImage)

# dilated = cv.dilate(canny,np.ones((5,5)),iterations=1) ##KERNEL VERİRKEN np.ones() ile ver yoksa çalışmıyor.
# cv.imshow("Dilated",dilated)

# erodedLess = cv.erode(dilated,np.ones((2,2)),iterations=1) ##KERNEL VERİRKEN np.ones() ile ver yoksa çalışmıyor.
# cv.imshow("ERODED LESS",erodedLess)

# erodedMore = cv.erode(dilated,np.ones((8,8)),iterations=1)
# cv.imshow("ERODED MORE",erodedMore)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# def rescaleFrame(frame,scale= 0.75): #EN BOY ORANINI HER ZAMAN KORUR
#     height = int(frame.shape[0] * scale)
#     width = int(frame.shape[1] * scale)
#     dimension = (width,height)
#     return cv.resize(frame,dimension,cv.INTER_AREA)

# parkImage = cv.imread("Photos\park.jpg")
# cv.imshow("Park",parkImage)

# parkImageRescale = rescaleFrame(parkImage,0.50)
# cv.imshow("Rescale",parkImageRescale)

# parkImageResize = cv.resize(parkImage,(300,200),cv.INTER_AREA) #BURDA DİREKT BİZ VERİYORUZ EN BOYU O YÜZDEN RESİM BOZULABİLİR.
# cv.imshow("Resize", parkImageResize)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# groupImage = cv.imread("Photos\group 1.jpg")
# cv.imshow("Group",groupImage)

# cropped = groupImage[180:350,270:400]
# cv.imshow("Cropped",cropped)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)

# ladyImage = cv.imread("Photos\lady.jpg")
# cv.imshow("Lady",ladyImage)

# translated1 = translate(ladyImage,100,100)
# cv.imshow("TRANSLATED - 1", translated1)

# translated2 = translate(ladyImage,-100,50)
# cv.imshow("TRANSLATED - 2",translated2)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# def rotate(img,angle,rotPoint= None):
#     (width,height) = img.shape[:2]

#     if rotPoint == None:
#         rotPoint = (width//2,height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions = (width,height)

#     return cv.warpAffine(img,rotMat,dimensions)

# ladyImage = cv.imread("Photos\lady.jpg")
# cv.imshow("Lady",ladyImage)

# rotated1 = rotate(ladyImage,45)
# cv.imshow("ROTATED - 1",rotated1)

# rotated2 = rotate(ladyImage,-45)
# cv.imshow("ROTATED - 2",rotated2)

# rotated3 = rotate(ladyImage,225)
# cv.imshow("ROTATED - 3",rotated3)

# rotated4 = rotate(ladyImage,-225)
# cv.imshow("ROTATED - 4",rotated4)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# ladyImage = cv.imread("Photos\lady.jpg")
# cv.imshow("Lady",ladyImage)

# resized = cv.resize(ladyImage,(1000,500),interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized",resized)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()

#--------------------------------------------------------------------------

# ladyImage = cv.imread("Photos\lady.jpg")
# cv.imshow("Lady",ladyImage)

# flippedVertical = cv.flip(ladyImage,0)
# cv.imshow("VERTICAL", flippedVertical)

# flippedHorizontal = cv.flip(ladyImage,1)
# cv.imshow("HORIZONTAL",flippedHorizontal)

# flippedVerticalAndHorizontal = cv.flip(ladyImage,-1)
# cv.imshow("VERTICAL AND HORIZONTAL",flippedVerticalAndHorizontal)

# key = cv.waitKey(0)

# if key == 27:
#     cv.destroyAllWindows()
