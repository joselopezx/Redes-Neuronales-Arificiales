# Redes-Neuronales-Arificiales
## Perceptron Simple
### Ajuste de pesos  
w(k+1) = w(k) + ne(k)x(k)
### Error
e(k) = d(k) - y(k)
### Ajuste de bias
b(k+1) = b(k) + ne(k) * 1
### Ejercicio 
**Funcion de activacion :** Funcion Signo -> si φ(Vn) > 0 y = 1 , si φ(Vn) <= 0 y = -1  
**Pesos iniciales :** W1 = 0, W2 = 0  
**Valor de umbral "BIAS" :** b = 0  
**N = 1**
| X(1) | X(2) |Y |
|-------|----------|--------|  
|2|1|1|  
|1|-1|-1|  
|2|-2|-1|  
|3|1|1|  
#### ITERACION 1  
x[2,1]  d=1  
Vn = (2)(0) + (1)(0) + 0 = 0  
φ(0) = -1  
y = -1 -> e = 1 - (-1) = 2  
  w = [0,0] + (1)(2)[2,1] = [0,0] + [4,2] = [4,2] -> W1, W2  
  b = 0 + (1)(2)(1) = 2
