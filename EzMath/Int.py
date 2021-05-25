"""
Este programa utiliza el método de Simpson para calcular integrales númericas.
"""
import numpy as np
import matplotlib.pyplot as plt

class integrate():
    def __init__(self,a,b,Eq):
        self.a = a
        self.b = b
        self.Eq = Eq
    def result_int(self):
        s = 0
        n = 10000
        dx = (self.b-self.a)/n
        for i in range(n):
            xi = self.a + i*dx
            x = self.a + (i+1)*dx
            s += (f(xi,self.Eq)+4*f((xi+x)/2,self.Eq)+f(x,self.Eq))*dx/6
        return round(s,4)
    def plot_int(self):
        x = np.arange(self.a-1,self.b+1,0.01)
        x2 = np.arange(self.a,self.b,0.01)
        y2 = f(x2,self.Eq)
        y = f(x,self.Eq)
        plt.plot(x,y,color="#023e8a")
        plt.fill_between(x2,y2,color="#48cae4")
        plt.savefig("Images/Integral.png")
        plt.clf()


def f(x,eq):
    f = eval(eq)
    return f

