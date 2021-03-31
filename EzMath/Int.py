"""
Este programa utiliza el método de Simpson para calcular integrales númericas.
"""
import numpy as np

print("Este programa calcula integrales de la forma:")
print("\\int_{a}^{b}f(x)dx")
a = float(input("Ingrese el valor de a "))
b = float(input("Ingrese el valor de b "))
Eq = input("Ingrese la función f(x) en sintaxis de python: ")
n=25
dx=(b-a)/n
s = 0

def f(x):
    f = eval(Eq)
    return f

for i in range(n):
    xi = a + i*dx
    x = a + (i+1)*dx
    s += (f(xi)+4*f((xi+x)/2)+f(x))*dx/6

print("El valor de la integral desde ",a,"hasta",b,"de "+Eq+ " es:",s)
