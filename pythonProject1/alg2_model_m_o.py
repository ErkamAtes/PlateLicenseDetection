import cv2
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

path = "karakterseti/"

siniflar = os.listdir(path)
batch_sayisi = 0
urls = [] #Ex: karakterseti/1/1.jpg
sinifs = []

for sinif in  siniflar:
    resimler = os.listdir(path+sinif)
    for resim in resimler:
        urls.append(path+sinif+"/"+resim)
        sinifs.append(sinif)
        batch_sayisi+=1

df = pd.DataFrame({"adres":urls,"sinif":sinifs})
#200x200
def islem(img):
    yeni_boy = img.reshape((1600,5,5))
    orts = []
    for parca in yeni_boy:
        ort = np.mean(parca)
        orts.append(ort)
    orts = np.array(orts)
    orts = orts.reshape(1600)
    return orts

def on_isle(img):
    return img/255

target_size = (200,200)
batch_size = batch_sayisi





