"""
Este programa utiliza el método de Simpson para calcular integrales númericas.
"""
import numpy as np

class integrate():
    def __init__(self,a,b,Eq):
        self.a = a
        self.b = b
        self.Eq = Eq
    def I(self):
        s = 0
        n = 10000
        dx = (self.b-self.a)/n
        for i in range(n):
            xi = self.a + i*dx
            x = self.a + (i+1)*dx
            s += (f(xi,self.Eq)+4*f((xi+x)/2,self.Eq)+f(x,self.Eq))*dx/6
            r = "El valor de la integral desde "+str(self.a)+" hasta "+str(self.b)+" de "+str(self.Eq)+" es: "+str(s)
        return r

def f(x,eq):
    f = eval(eq)
    return f

