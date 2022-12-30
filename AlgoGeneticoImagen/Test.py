"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""

from ImagenFiguras import ImagenFiguras
from AlgoritmoGen import AlgoritmoGen
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time

# time_duration = 3.5
# time.sleep(.5)

numFiguras = 1000
numPob = 300
# imgOrig = cv2.imread("Scooby.jpg")
# print("shape: ", imgOrig.shape)
# imgOrig = cv2.resize(imgOrig, (320,232)
imgOrig = cv2.imread("Harry2.jpg")
imgAux = 255*np.ones(imgOrig.shape, dtype = np.uint8)
print("shape: ", imgOrig.shape)


ag = AlgoritmoGen(300, imgOrig, numFiguras)
ag.init()
cv2.imshow("Imagen Original", imgOrig)

for i in range(100000):
    ag.evolucion()
    imgMejor = ag.muestraMejor(i)
    imgAux = imgMejor.getImagenGen()
    cv2.imshow("Imagen La mejor", imgAux)
    print("generacion: ",i)
    cv2.waitKey(10)
    # plt.figure(1)
    # plt.subplot(1,2,1)
    # plt.imshow(imgOrig)
    # plt.title("Original ")
    # plt.subplot(1,2,2)
    # plt.imshow(imgAux)
    # plt.title("La mejor")
    # plt.show()
##print(i)
# bgr = [255,255,0]
# pos = [50,80]
# cv2.circle(imgAux, (pos),5, (bgr),-1)

#
# imF = ImagenFiguras(numFiguras, imgOrig.shape)
# imF.init()
# imgAux = imF.getImagenGen()
# diferencia = cv2.subtract(imgOrig, imgAux)
#
# b, g, r = cv2.split(diferencia)
# print("b ", b)
# print(cv2.countNonZero(b))
#
#

# print(imgOrig.shape)
# print("Prueba1: ",imgOrig.shape[1])

# cv2.imshow("Imagen Prueba", imgAux)
#cv2.imshow("Imagen Diferencia", diferencia)

# cv2.waitKey(0)
