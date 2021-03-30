"""
Este programa utiliza el método de Euler para graficar la función y solución a una
ecuación diferencial de primer orden.
"""
import matplotlib.pyplot as plt
import numpy as np

n = 1000
x0 = float(input("Ingrese la coordenada x del punto P(x0,y0) de condición inicial: "))
y0 = float(input("Ingrese la coordenada x del punto P(x0,y0) de condición inicial: "))
x_lim = float(input("Ingrese el valor máximo de x donde quiere graficar: "))
h = (x_lim-x0)/n
y1 = [y0]
Eq = input("Ingrese la ecuación diferencial y' = ")

def f(x,y):
    f = eval(Eq)
    return f

for i in range(0,n):
    y2 = y1[i]+h*f(x0+i*h,y1[i])
    y1.append(y2)

y = np.array(y1)
x = np.arange(x0,x_lim+h,h)
plt.plot(x,y,linestyle='solid',color='blue')
plt.show()