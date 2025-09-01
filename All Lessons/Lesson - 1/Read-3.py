#VİDEO OKUMA VE GÖSTERME
import cv2 as cv

vid = cv.VideoCapture("Videos\dog.mp4") #BU KISIM VİDEO SOURCE'UNU YAZIYORSUN 0 GİRERSEN WEBCAMIN AÇILIR

while True:
    isTrue, frame = vid.read() #vid.read() FRAME FRAME VİDEOYU OKUR ve isTrue değerine değer okunduysa TRUE okunamadıysa FALSE döner.

    if isTrue:
        cv.imshow("Video",frame) #OKUNAN HER KAREYİ PENCEREYE GÖSTER
    else:
        print("Frame doesn't exist")
        break
    
    if cv.waitKey(20) & 0xFF == ord("d"): #0xFF yazıyoruz sonra ord yazıp bir tane tuş yazıyoruz çıkış işlemi yapmak için.
        break

vid.release() #EĞER BUNU YAZMAZSAN WEBCAMINI DİĞER UYGULAMALAR KULLANAMAZ VEYA VİDEOYU HEP AÇIK GÖZÜKÜR ARKADA
cv.destroyAllWindows() #BU SADECE OPENCV PENCERELERİNİ KAPATIYOR
