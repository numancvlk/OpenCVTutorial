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