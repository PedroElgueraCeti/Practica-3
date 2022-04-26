#Pedro Miguel Elguera Mora 19110148

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import cv2 #Opencv
import skimage
from skimage import io
import math

#Imágenes Iniciales
img1 = cv2.imread('mustang.jpg', 1)
img2 = cv2.imread('camaro.jpg', 1)

#Dimencionamiento en bruto
Redimg1 = cv2.resize(img1, (200, 200))
Redimg2 = cv2.resize(img2, (200, 200))

#De matriz BGR a RGB
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
Redimg2 = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2RGB)

fila = 4
columna = 3
fig = plt.figure(figsize=(10,7), constrained_layout=True) 
fig.add_subplot(fila,columna,1)
plt.imshow(Redimg1)
plt.axis('off')
plt.title("Imagen 1")

fig.add_subplot(fila,columna,4)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([Redimg1], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.title("Histograma img 1")
fig.add_subplot(fila,columna,7)
#aqui va el calculo del ecualizado
img_to_yuv = cv2.cvtColor(Redimg1,cv2.COLOR_RGB2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
equaimg1 = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2RGB)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([equaimg1], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])
    plt.ylim([0,1000])
plt.title("Histograma img 1 Ecualizada")

fig.add_subplot(fila,columna,10)
plt.imshow(equaimg1)
plt.axis('off')
plt.title("Imagen 1 Ecualizada")

#-------------------------Segunda Imagen
fig.add_subplot(fila,columna,3)
plt.imshow(Redimg2)
plt.axis('off')
plt.title("Imagen 2")

fig.add_subplot(fila,columna,6)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([Redimg2], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.title("Histograma img 2")
fig.add_subplot(fila,columna,9)
#aqui va el calculo del ecualizado
img_to_yuv = cv2.cvtColor(Redimg2,cv2.COLOR_RGB2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
equaimg2 = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2RGB)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([equaimg2], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])
    plt.ylim([0,1000])
plt.title("Histograma img 2 Ecualizada")

fig.add_subplot(fila,columna,12)
plt.imshow(equaimg2)
plt.axis('off')
plt.title("Imagen 2 Ecualizada")

#----------------Operacion-----------------

fig.add_subplot(fila,columna,2)
Redop=cv2.add(Redimg1,Redimg2)
plt.imshow(Redop)
plt.axis('off')
plt.title("Imagen 2 Suma")

fig.add_subplot(fila,columna,5)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([Redop], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.title("Histograma Suma")
fig.add_subplot(fila,columna,8)
#aqui va el calculo del ecualizado
img_to_yuv = cv2.cvtColor(Redop,cv2.COLOR_RGB2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
equaimgOp = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2RGB)
color = ('g','b','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([equaimgOp], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])
    plt.ylim([0,1000])
plt.title("Histograma img Suma Ecualizada")

fig.add_subplot(fila,columna,11)
plt.imshow(equaimgOp)
plt.axis('off')
plt.title("Imagen Suma Ecualizada")


plt.show()
