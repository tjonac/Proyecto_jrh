import numpy as np
import matplotlib.pyplot as plt

print("Este programa calcula derivadas númericas. ")

a = float(input("Ingrese el valor donde desea evaluar la derivada: "))
Eq = input("Ingrese la función f(x) en sintaxis de python: ")
h = 0.000001

def f(x):
    f = eval(Eq)
    return f

Dx = (f(a+h)-f(a))/h
print("El valor de la derivada de ", Eq, " en x=",a," es:", Dx)