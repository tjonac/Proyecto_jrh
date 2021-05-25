"""
Este programa utiliza la definición de la derivada de f en un punto x=a
"""
import numpy as np
import matplotlib.pyplot as plt

class derivative():
    def __init__(self,a,Eq):
        self.a = a
        self.Eq = Eq
        self.h = 0.00001
        self.Dx = (f(self.a+self.h,self.Eq)-f(self.a,self.Eq))/self.h
    
    def result_dx(self):
        return round(self.Dx,4)
    def plot_dx(self):
        x = np.arange(self.a-5,self.a+5+0.00001,0.00001)
        x2 = np.arange(self.a-2,self.a+2,0.00001)
        y2 = self.Dx*(x2-self.a)+f(self.a,self.Eq)
        y = f(x,self.Eq)
        plt.plot(x2,y2,color="#48cae4")
        plt.plot(x,y,color="#023e8a")
        plt.savefig("Images/Derivada.png")
        plt.clf()


def f(x,eq):
    f = eval(eq)
    return f
