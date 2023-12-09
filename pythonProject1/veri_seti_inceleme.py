import os
import matplotlib.pyplot as plt
import cv2
from alg_1_plakatespiti import plaka_konum_don
"""
#1.Alg Veri Inceleme
#-------------------
#veriseti klasörüne ulaşıyoruz
veri = os.listdir("veriseti")
#klasörün içinde gezinerek resimlere ulaşıyoruz
for image_url in veri:
    img = cv2.imread("veriseti/" + image_url) #resimlerin urllerini okuyoruz Ex: "veriseti/1.png"  ve bgr değerlerini döndürecek bize
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #matplotlib kütüphanesinden görselleştirebilmemiz için rgb değerine döndürüyoruz
    img = cv2.resize(img, (500,500))
    plt.imshow(img) #görselleştirdik
    plt.show()
"""


#2.Alg Veri Inceleme
#-------------------

veri = os.listdir("veriseti")
#klasörün içinde gezinerek resimlere ulaşıyoruz
for image_url in veri:
    img = cv2.imread("veriseti/" + image_url) #resimlerin urllerini okuyoruz Ex: "veriseti/1.png"  ve bgr değerlerini döndürecek bize
    img = cv2.resize(img, (500,500))
    plaka = plaka_konum_don(img) #x,y,w,h
    x,y,w,h = plaka
    if(w>h):
        plaka_bgr = img[y:y+h,x:x+w].copy()
    else:
        plaka_bgr = img[y:y + w, x:x + h].copy()


    img2 = cv2.cvtColor(plaka_bgr,cv2.COLOR_BGR2RGB)  # matplotlib kütüphanesinden görselleştirebilmemiz için rgb değerine döndürüyoruz
    plt.imshow(img) #görselleştirdik
    plt.show()