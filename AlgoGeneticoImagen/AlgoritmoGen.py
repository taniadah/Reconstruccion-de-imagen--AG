"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango
Unidad de Aprendizaje:Sistemas Expertos
@author: taniadelangel
"""
from FuncionAptitud import FuncionAptitud as FunAp
from Seleccion import Seleccion
from ImagenFiguras import ImagenFiguras as imgFig
from Poblacion import Poblacion
import numpy as np
import random


class AlgoritmoGen:
    def __init__(self, size, imgObj, numFig):
        '''
        recibe la imagen, el tamaño de la poblacion y conforme al tamaño de la imagen objetivo, sera el tamaño de nuestra imagen "individuo"
        '''
        self.shapeImg = imgObj.shape
        self.size = size
        self.pob = None
        self.imgObj = imgObj
        self.numFig = numFig
        self.numPix = imgObj.shape[0]*imgObj.shape[1]

    def init(self):
        pob = Poblacion(self.imgObj,self.numFig,self.size)
        pob.init()
        self.pob = pob
        self.seleccion = Seleccion()
        self.fa = FunAp(self.imgObj)

    def muestraMejor(self, gen):
        #aptitudes = [self.fa.evaluate(img, self.numPix) for img in self.pob.poblacion]
        #indice = aptitudes.index(min(aptitudes))
        #print("aptitud mejor: ", min(aptitudes))
        #print("En el indice: ", (aptitudes.index(min(aptitudes))))
        imgMejor = self.pob.poblacion[0]
        return imgMejor

    def evolucion(self):
        # 1) Evaluar individuos
        poblacion = self.pob.poblacion                             # Aislamos la poblacion
        aptitudes = [self.fa.evaluate(ind, self.numPix) for ind in self.pob.poblacion]   # Obtenemos sus aptitutes

        # 2) Seleccionar padres para cruza
        k = int(self.size/2)                          # Divide el tamaño de la poblacion en 2
        if k%2 == 1:                                  # Condicional por si k es impar, por lo que
            k += 1                                    # le sumamos 1 para evitar problemas en la cruza
        idx = self.seleccion.selecciona(aptitudes, k) # Guarda k individuos seleccionados, se le manda
                                                      # las aptitudes y un numero k

        #3) Generar hijos (cruza)
        descendencia = []                   # Arreglo para guardar la descendencia
        for i in list(range(0,k-1,2)):      # Ciclo para recorrer la poblacion cada 2 individuos
            ip = idx[i]                     # Selecciona el indice del padre
            im = idx[i+1]                   # Selecciona el indice de la madre
            papa = poblacion[ip]            # Apartamos al padre guardadolo en una variable
            mama = poblacion[im]            # Apartamos a la madre guardadola en una variable
            hijos = papa.cruza(mama)       # Cruzamos al papa con la mama y obtenemos a los hijos
            descendencia.append(hijos[0])   # Agregamos a la descendencia el primer hijo
            descendencia.append(hijos[1])   # Agregamos a la descendencia el segundo hijo


        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.1))   # Convierte a entero un numero redondeado
                                                           # del 1 porciento del tamaño de la
                                                           # descendencia siendo el numero obtenido
                                                           # la cantidad de individuos a mutar
        for i in range(totalMutar):                        # Ciclo para mutar individuos segun el
                                                           # numero obtenido anteriormente, donde
            idx = random.choice(range(len(descendencia)))  # los individuos son elegidos
            descendencia[idx].mutar()                      # aleatoriamente


        # 5) Evaluar hijos
        for hijo in descendencia:                                # Ciclo para recorrer la descendencia y
            poblacion.append(hijo)                               # agregar los hijos a la poblacion

        aptitudes = [self.fa.evaluate(ind, self.numPix) for ind in self.pob.poblacion]  # Obtengo las aptitutes de la poblacion

        # 6) Seleccionar miembros de la siguiente población
        # ELITISMO!!!!!
        idxMejor = np.argmin(aptitudes)                         # Obtiene al individuo con la mejor
                                                                # aptitud
        siguientePob = []                                       # Se crea la lista de individuos de la
                                                                # siguiente generación
        siguientePob.append(poblacion[idxMejor])                # Agrega a la siguiente poblacion al
                                                                # individuo con la mejor aptitud
        idx = self.seleccion.selecciona(aptitudes, self.size)   # Selecciona a los siguientes individuos

        for i in idx:                                           # Ciclo para reccorer a los individuos
            siguientePob.append(poblacion[i])                   # seleccionados y agregarlos en la
                                                                # siguiente poblacion

        self.pob.poblacion = siguientePob                       # Guardo la siguiente poblacion para
                                                                # su evolución

    def evaluarImagenes(self):
        #1. Evaluar a los individuos
        '''Mediante la clase FuncionAptitud se evaluara la aptitud de cada individuo en cada poblacion'''
        poblacion = self.pob.poblacion
        aptitudes = [self.fa.evaluate(img, self.numPix) for img in poblacion]

        self.aptitudes = aptitudes

    def selec(self):
        #2) Seleccionar padres para cruza
        "Se dividira la poblacion a la mitad y de esa mitad se escogera a los padres, de tal manera que se le va a dar prioridad a aquellos con mejor aptitud, para esto hacemos uso de la clase seleccion"
        aptitudes = self.aptitudes
        mit = int(self.size/2)
        if mit%2 == 1:
            mit+=1
        #idx son los indices de los seleccionados que regresa la funcion selecciona de la clase seleccion
        idx =self.seleccion.selecciona(aptitudes, mit)
        self.mit = mit
        self.idx = idx


    def cruzar(self):
        #Cruza : Generar hijos
        '''se vaa crear una lista donde se guardaran a los hijos, se mandara a llamar al metodo cruza de la clase ImagenFiguras, mediante los padres elegidos (idx) se tomara un tercio de los genes de uno y de otro, variando es un tercio porque es cruza por dos puntos'''
        poblacion = self.pob.poblacion
        cruzas = []
        idx = self.idx

        for i in list(range(0, self.mit-1, 2)):
            ip = idx[i]
            im = idx[i+1]
            papa = poblacion[ip]
            mama = poblacion[im]

            imgHijas = papa.cruza(mama)
            cruzas.append(imgHijas[0])
            cruzas.append(imgHijas[1])

        self.cruzas = cruzas

    def mutar(self):
        #4.Mutar el 5%
        '''sacamos el porcentaje de individuos que se van a mutar de la lista cruzas
        se escogeran los individuos que se mutaran'''
        cruzas = self.cruzas
        #Se multiplica por 0.1 ya que como es la descendencia es la mitad de la poblacion total por lo que al sacar el .1 de la descendencia se toma el .05 (5%) de la poblacion total
        totalMutar = int(np.ceil(len(self.cruzas)*0.1))
        idx = self.idx
        for i in range(totalMutar):
            idx = random.choice(range(len(self.cruzas)))
            cruzas[idx].mutar()

    def evaluacionYSeleccion(self):
        '''colocamos a los hijos en la lista de la poblacion para que hijos y padres esten juntos'''

        poblacion = self.pob.poblacion
        cruzas = self.cruzas
        print("poner hijos padres juntos")
        for imgHija in cruzas:
            poblacion.append(imgHija)

        #calculo aptitudes de todos
        # print("Evalua aptitudes")

        aptitudes = [self.fa.evaluate(img, self.numPix) for img in poblacion]

        #Elitismo
        # print("Elitismo")

        idxMejor = np.argmax(aptitudes)
        sigPob = []
        sigPob.append(poblacion[idxMejor])

        #Selecciono indices de individuos para la siguiente generacion
        # print("Seleccion")

        idx = self.seleccion.selecciona(aptitudes, self.size)

        #lista de individuos de la siguiente generacion
        # print("poner sig gen")

        for i in idx:
            sigPob.append(poblacion[i])

        self.pob.poblacion = sigPob
