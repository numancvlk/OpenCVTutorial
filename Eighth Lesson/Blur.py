#Blurring
import cv2 as cv

cats = cv.imread("Photos\cats.jpg")
cv.imshow("Cats",cats)

# Gaussian Blur
# - Komşu pikselleri Gaussian dağılıma göre ağırlıklandırır
# - (7,7): kernel boyutu (tek sayı olmalı), ne kadar büyük olursa o kadar bulanık
# - cv.BORDER_DEFAULT: sınır pikseller için varsayılan yöntem

gaussianBlur = cv.GaussianBlur(cats,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur", gaussianBlur)

# Averaging (Mean Blur)
# - Kernel içindeki tüm piksellerin ortalamasını alır
# - Daha basit ama detayları daha çok kaybettirir
# - (7,7): kernel boyutu (örn: 7x7 penceredeki değerlerin ortalaması alınır)
averageBlur = cv.blur(cats,(7,7))
cv.imshow("Average Blur", averageBlur)

# Median Blur
# - Kernel içindeki piksellerin ortancasını (median) alır
# - Gürültü azaltmada (özellikle "salt & pepper" noise) çok iyidir
medianBlur = cv.medianBlur(cats, 7) #KERNEL BOYUTUNU DİREKT INTEGER GİRİYORUZ DİKKAT!
cv.imshow("Median Blur", medianBlur)

# Bilateral Blur
# - Hem uzamsal yakınlığa (komşuluk) hem de renk benzerliğine bakar
# - Bu sayede kenarları korur, sadece benzer renk bölgelerini bulanıklaştırır
# - Parametreler:
#   10  → d (komşuluk çapı)
#   35  → sigmaColor (renk farkı eşiği, büyük olursa daha fazla renk bulanıklaşır)
#   25  → sigmaSpace (uzamsal mesafe, büyük olursa uzak pikseller de dikkate alınır)
bilateralBlur = cv.bilateralFilter(cats,20,35,25)
cv.imshow("Bilateral Blur", bilateralBlur)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()