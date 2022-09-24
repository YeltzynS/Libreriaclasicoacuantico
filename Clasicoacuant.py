from adicicionvectocomp.py import accion_matriz, normavect
import numpy as np
import matplotlib.pyplot as plot
def canicas(matriz, vector, clicks):
    matriz = np.array(matriz)
    vector = np.array(vector)
    vector = np.array([vector])
    vector = (vector.T)
    mult = vector
    resp = 0
    for i in range(0, clicks):
        resp = np.dot(matriz,mult)
        mult = resp
    return resp

def sistemaProbabilistico(mat, vec, clicks):
    for i in range(clicks):
        vec = accion_matriz(mat, vec)
    return vec
def doblerendija(mat, vec, clicks):
    for i in range(clicks):
        vec = accion_matriz(mat, vec)
    return normavect(vec)
def multipleSlit(mat, vec, times):
    return sistemaProbabilistico(mat, vec, times)

def graf_diagrama(v):
    # Funcion que crea y guarda un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se guarda en el computador con un formato de imagen.
    ejes = len(v)
    x = np.array([x for x in range(ejes)])
    y = np.array([round(v[x]*100, 3) for x in range(ejes)])
    plot.bar(x, y, color="gray", align="center")
    plot.title("Vector_Probabilidades")
    plot.savefig("Vector_Probabilidades.png")
    plot.show()