"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""

from ImagenFiguras import ImagenFiguras


class Poblacion:
    """si el tamaño de poblacion no es definido antes tendra
    una poblacion de 300, se le pasa la imagen original y se
    saca el tamaño de esta con shape para definir el tamaño de
    cada individuo (imagen generada)"""
    #
    def __init__(self, imgOrig, numFig,tam = 300):
        self.tam = tam
        self.imaObj = imgOrig
        self.tamI = self.imaObj.shape
        self.numFig = numFig


    def init(self):
        poblacion = []
        for i in range(self.tam):
            imF = ImagenFiguras(self.numFig, self.tamI)
            imF.init()
            imgAux = imF.getImagenGen()
            poblacion.append(imF)
        self.poblacion = poblacion
