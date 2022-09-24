#import matplotlib.pyplot as plot
#import numpy as np
from adicionvectocomp.py import accion_matriz , normavec

def accion_bool_matriz_vector(matriz,vector):
    """
    Funicion que determina la accion de una matriz booleana con un vector booleano.
    :param matriz: matriz booleana
    :param vector: vector booleano
    :return: vector que representa la accion de la matriz por el vector.
    """
    filas = len(matriz)
    colum = len(matriz[0])
    longitud = len(vector)
    if colum == longitud:
        res = [False for c in range(filas)]
        for i in range(filas):
            condi = True
            for j in range(colum):
                condi = matriz[i][j] and vector[j]
                res[i] = res[i] or condi
        return res
    else:
        print("La matriz y el vector no se pueden multiplicar")

def canicas_clicks(matriz,vector,clicks):
    """
    Funcion que simula el experimento de la canicas con coeficiente booleanos.
    :param matriz: matriz booleana
    :param vector: vector booleano
    :param clicks: clicks que deseo calcular
    :return: vector.
    """
    for i in range(clicks):
        vector = accion_bool_matriz_vector(matriz,vector)
    return vector

def probabilistico_clicks(matriz,vector,clicks):
    """
    Funcion que simula las múltiples rendijas clásico probabilístico,
    con más de dos rendijas.
    :param matriz: matriz inicial
    :param vector: vector estado
    :param clicks: cliscks que deseo calcular
    :return: vector.
    """
    for i in range(clicks):
        vector = accion_matriz(matriz,vector)
    return vector

def cuantico_clicks(matriz,vector,clicks):
    """
    Funcion que simula el experimento de multiples rendijas.
    :param matriz: matriz inicial
    :param vector: vector estado
    :param clicks: clicks que desdeo calcular
    :return: lista con las probabilidades
    """
    proba = []
    for i in range(clicks):
        vector = accion_matriz(matriz,vector)
    for elemento in vector:
        elemento = (normavec([elemento])[0])**2
        proba = proba + [elemento]
    return proba

#def grafico(vector):
    #"""
    #Funcion que muestra un diagrama de barras que representa las probabilidades
    #de un vector estado.
    #:param vector: vector estado
    #:return: Diagrama de barras en formato .png
    #"""
    #ejes = len(vector)
    #x = np.array([x for x in range(ejes)])
    #y = np.array([round(vector[x]*100, 3) for x in range(ejes)])
    #plot.bar(x, y, color="blue", align="center")
    #plot.title("Vector Probabilidades")
    #plot.savefig("Vector_Probabilidades.png")
    #plot.show()
