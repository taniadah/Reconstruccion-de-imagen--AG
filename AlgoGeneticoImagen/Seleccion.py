"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""

import numpy as np
import random


class Seleccion:
    '''
    Se hace la seleccion de los nuevos individuos conforme a sus aptitudes
    Nota: Se le da preferencia a los individuos con mayor aptitud, pero si alguno tiene aptitud baja, tiene posibilidad de ser elegido, por eso se agrega un pequeño valor (.01)

    Se calcula la probabilidad de ser elegido mediante la funcion de softmax, la cual saca la probabilidad de un individuo según su aptitud.

    esas probabilidades de guardan en una lista y para finalizar se scan los indices de esas porbabilidades y se devuelve el indice de donde esta guardado el individuo y la probabilidad de ser elegido
    '''


    def selecciona(self, aptitudes, k = 2):
        aux = aptitudes.copy()
        # print("aptitudes1")
        # print(aptitudes)
        aux.sort(reverse=False)
        mejoresAptitudes = []                          # Arreglo para los mejores individuos

        for i in range(k):
            idxMejor = aptitudes.index(aux[i])
            #print("idx: ",idxMejor)

            mejoresAptitudes.append(idxMejor)    # al arreglo de mejoresInd, luego se borran todas las
                                                 # coincidencias del mismo individuo del arreglo
        return mejoresAptitudes
