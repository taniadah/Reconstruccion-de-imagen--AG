"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""
import cv2
import numpy as np
class FuncionAptitud:
    """docstring for FuncionAptitud."""
    def __init__(self, imgObjetivo):
        self.imgObjetivo = imgObjetivo


    def evaluate(self, imgGen, cobj):
        imgAux = imgGen.getImagenGen()
        diferencia = cv2.absdiff(imgAux ,self.imgObjetivo)
        # diferencia = cv2.subtract(self.imgObjetivo, imgAux)
        # b =  [abs(ele) for ele in b]
        # g =  [abs(ele) for ele in g]
        # r =  [abs(ele) for ele in r]
        # b, g, r = cv2.split(diferencia)
        #
        # #print("b ", b)
        # sumb = np.sum(b)
        # sumg = np.sum(g)
        # sumr = np.sum(r)
        sumDif = np.sum(diferencia, axis=0)

        cont = sum(sumDif)
        cont = sum(cont)
        # print("Cont")
        # print(cont)

        #print(cv2.countNonZero(b))
        #print("cont:",cont)
        return cont
