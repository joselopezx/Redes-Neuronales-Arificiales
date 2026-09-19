import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random 

PUNTOS = {'X(1)':[0,0,0,1,1,1,1], 
          'X(2)':[0,1,1,0,0,1,1],
          'X(3)':[1,0,1,0,1,0,1], 
          'Y'   :[1,2,3,4,5,6,7]}
PUNTOS_DF = pd.DataFrame(PUNTOS)

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


def Adeline(df, d, pesos, BIAS, N):
    filas = df.shape[0]
    columnas = df.shape[1]
    e=1
    errores = []
    for i in range (0,10):
        print(f'PESOS -> {pesos}, ERROR -> {e}')
        for j in range(0,filas):
            datosFila = df.iloc[j].values
            y = Vn(datosFila, pesos, BIAS)
            e = error(d[j], y)
            for k in range (0,columnas):
                pesos[k] = ajustePesos(pesos[k], df.iloc[j, k], e, N)
            BIAS = ajusteBias(e, BIAS, N)
        errores.append(e)

    print(f'PESOS -> {pesos},  BIAS -> {BIAS}, ERROR -> {e}')    
    plt.plot(errores)
    plt.show()

d = PUNTOS_DF['Y']
PUNTOS_DF = PUNTOS_DF.drop('Y', axis=1)
print('------ EJERCICIO 1 ---------')
pesos = []
for i in range (0,3):
    pesos.append(random.randint(1,5))
Adeline(PUNTOS_DF, d, pesos = pesos, BIAS = 0, N = 0.3)




