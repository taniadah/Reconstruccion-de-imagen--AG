"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""

import random
import numpy as np


class Figura:
    """docstring forIndividuo."""

    def __init__(self, dimensiones):
        self.radios = [0,0]
        self.posicion = [0,0]
        self.color  = [0,0,0]
        self.dimensiones = dimensiones;


    def init(self):
        posY = random.randint(0, self.dimensiones[0])
        posX = random.randint(0, self.dimensiones[1])
        rMayor = random.randint(0, 10)
        rMenor = random.randint(0, 10)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        r = random.randint(0, 255)

        self.radios = [rMayor, rMenor]
        self.posicion = [posX, posY]
        self.color = [b,g,r]
