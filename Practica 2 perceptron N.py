import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

PUNTOS = {'X(1)':[3,2,4,1,0.5,1], 
          'X(2)':[2,3,1,1,1,0.5],
          'X(3)':[1,1,0.5,3,2,4],
          'X(4)':[1,1,0.5,3,2,4], 
          'Y':[1,1,1,-1,-1,-1]}
PUNTOS_DF = pd.DataFrame(PUNTOS)

PUNTOS2 = {'X(1)':[3,2,4,1,0.5,1], 
          'X(2)':[2,3,1,1,1,0.5],
          'Y':[1,1,1,-1,-1,-1]}
PUNTOS2_DF = pd.DataFrame(PUNTOS2)

def funcionActivacion(Vn):
    if Vn > 0:
        return 1
    else:
        return -1

def ajustePesos(W, X,e, N):
    return W + N *  e * X

def ajusteBias(e, nBias, N):
    return nBias + N*e*1

def error(d,y):
    return d-y

def Vn(features, pesos, bias):
    #Vn = X(n)*W(n) + X(n)*W(n) + ... + d
    tamFeatures = len(features)
    tamPesos = len(pesos)
    res = 0
    if tamFeatures==tamPesos:
        for x in range (0,tamPesos):
            res = res + features[x]*pesos[x]
        return res + bias
    else:
        return 0


def Percetron(df, d, pesos, BIAS, N, EPOCAS):
    filas = df.shape[0]
    columnas = df.shape[1]
    for x in range (0,EPOCAS):
        for i in range(0,filas):
            datosFila = df.iloc[i].values
            y = funcionActivacion(Vn(datosFila, pesos, BIAS))
            e = error(d[i], y)
            if e != 0:
                for j in range (0,columnas):
                    pesos[j] = ajustePesos(pesos[j], df.iloc[i, j], e, N)
                BIAS = ajusteBias(e, BIAS, N)

    print(f'PESOS -> {pesos},  BIAS -> {BIAS}')    

d = PUNTOS_DF['Y']
PUNTOS_DF = PUNTOS_DF.drop('Y', axis=1)
print('------ EJERCICIO 1 ---------')
Percetron(PUNTOS_DF, d, pesos = [-10,-10,10,10], BIAS = 0.1, N = 0.2, EPOCAS = 7)
print('------ EJERCICIO 2 ---------')
d = PUNTOS2_DF['Y']
PUNTOS2_DF = PUNTOS2_DF.drop('Y', axis=1)
Percetron(PUNTOS2_DF, d, pesos = [5,1], BIAS = 1, N = 0.6, EPOCAS = 2)

