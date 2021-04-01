"""
Este programa utiliza la definición de la derivada de f en un punto x=a
"""
import numpy as np
import matplotlib.pyplot as plt

class derivative():
    def __init__(self,a,Eq):
        self.a = a
        self.Eq = Eq

    def derivate(self):
        h = 0.000001
        Dx = (f(self.a+h,self.Eq)-f(self.a,self.Eq))/h
        r = "El valor de la derivada de "+str(self.Eq)+" evaluada en x = "+str(self.a)+" es: "+str(Dx)
        return r
def f(x,eq):
    f = eval(eq)
    return f