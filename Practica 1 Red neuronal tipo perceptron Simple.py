import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

PUNTOS = {'X(1)':[2,1,2,3], 'X(2)':[1,-1,-2,1], 'Y':[1,-1,-1,1]}
PUNTOS_DF = pd.DataFrame(PUNTOS)

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

def Percetron(W1, W2, BIAS, N, EPOCAS):
    for x in range (0,EPOCAS):
        print(f'Iteracion {x+1}')
        print(f'W1 -> {W1}')
        print(f'W2 -> {W2}')
        print(f'BIAS -> {BIAS}')
        for i in range(0,4):
            #Vn = X1*W1 + X2*W2 + d
            x1 = PUNTOS_DF.iat[i,0]
            x2 = PUNTOS_DF.iat[i,1]
            d  = PUNTOS_DF.iat[i,2]
            Vn = x1*W1 + x2*W2 + BIAS
            y = funcionActivacion(Vn)
            e = error(d, y)
            if e != 0:
                W1 = ajustePesos(W1, x1,e, N)
                W2 = ajustePesos(W2, x2,e, N)
                BIAS = ajusteBias(e, BIAS, N)
    return W1, W2, BIAS

print('------ EJERCICIO 1 ---------')
w1e1, w2e1, b1 = Percetron(W1=0, W2 = 0, BIAS = 0, N = 1, EPOCAS = 10)
print('------ EJERCICIO 2 ---------')
w1e2, w2e2, b2 = Percetron(W1=5, W2 = 1, BIAS = 1, N = 0.6, EPOCAS = 20)

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=PUNTOS_DF,
    x='X(1)',
    y='X(2)',
    hue='Y',
    palette='coolwarm',
    s=150
)

x1_valores = np.linspace(0, 7, 100)


if w2e1 != 0:
    x2_e1 = -(w1e1 / w2e1) * x1_valores - (b1 / w2e1)
    plt.plot(x1_valores, x2_e1, color='purple', linestyle='--', linewidth=2, label='Frontera Ejercicio 1')
else:
    plt.axvline(x=-b1/w1e1, color='purple', linestyle='--', linewidth=2, label='Frontera Ejercicio 1 (Vertical)')

if w2e2 != 0:
    x2_e2 = -(w1e2 / w2e2) * x1_valores - (b2 / w2e2)
    plt.plot(x1_valores, x2_e2, color='green', linestyle='-', linewidth=2, label='Frontera Ejercicio 2')
else:
    plt.axvline(x=-b2/w1e2, color='green', linestyle='-', linewidth=2, label='Frontera Ejercicio 2 (Vertical)')


plt.title('Puntos', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.show()