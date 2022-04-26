#Pedro Miguel Elguera Mora 19110148

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import cv2 #Opencv
import skimage
from skimage import io
import math

#Imágenes Iniciales
img1 = cv2.imread('Ave1.jpg', 1)
img2 = cv2.imread('Ave2.jpg', 1)

#Dimencionamiento en bruto
Redimg1 = cv2.resize(img1, (200, 200))
Redimg2 = cv2.resize(img2, (200, 200))

#De matriz BGR a RGB
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
Redimg2 = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2RGB)

color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([Redimg1], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.imshow(Redimg1)
plt.show()