"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""

from Figura import Figura
import cv2
import numpy as np

class ImagenFiguras:
    """docstring forImagenOvalos."""

    def __init__(self, numFig, dimensiones):
        self.numFig = numFig
        self.shapeImgOr = dimensiones
        self.imagen = np.zeros((dimensiones), dtype = np.uint8)
        self.cromosoma = []


    def init(self):
        for i in range(self.numFig):
            fig = Figura(self.shapeImgOr)
            fig.init()
            #cv2.circle(self.imagen, tuple(fig.posicion), fig.radio, tuple(fig.color), -1)
            cv2.ellipse(self.imagen, fig.posicion, fig.radios, 0, 0, 360, fig.color, -1)
            self.cromosoma.append(fig)

    def creaFiguras(self):
        for i in range(self.numFig):
            fig = self.cromosoma[i]
            #cv2.circle(self.imagen, tuple(fig.posicion), fig.radio, tuple(fig.color), -1)
            cv2.ellipse(self.imagen, fig.posicion, fig.radios, 0, 0, 360, fig.color, -1)

    def getImagenGen(self):
        return self.imagen

    def cruza(self, madre):
        padre = self.cromosoma
        madre = madre.cromosoma

        cp1 = int(np.floor((self.numFig-1)/3.))
        cp2 = 2*cp1

        imgCrom1 = padre[0:cp1]
        imgCrom1.extend(madre[cp1:cp2])
        imgCrom1.extend(padre[cp2:])

        imgCrom2 = madre[0:cp1]
        imgCrom2.extend(padre[cp1:cp2])
        imgCrom2.extend(madre[cp2:])

        imgHija1 = ImagenFiguras(self.numFig, self.shapeImgOr)
        imgHija2 = ImagenFiguras(self.numFig, self.shapeImgOr)

        imgHija1.cromosoma = imgCrom1
        imgHija2.cromosoma = imgCrom2

        imgHija1.creaFiguras()
        imgHija2.creaFiguras()


        return[imgHija1, imgHija2]

    def mutar(self):
        idx = np.random.randint(self.numFig)
        fig = Figura(self.shapeImgOr);
        fig.init()
        cambiar = fig
        self.cromosoma[idx] = cambiar
        self.imagen = np.zeros((self.shapeImgOr), dtype = np.uint8)
        self.creaFiguras()
