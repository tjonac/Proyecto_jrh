"""
Este programa utiliza el método de Euler para graficar la función y solución a una
ecuación diferencial de primer orden.
"""
import matplotlib.pyplot as plt
import numpy as np

class euler_method():
    def __init__(self,xo,yo,x_lim, Eq):
        self.xo = xo
        self.yo = yo
        self.x_lim = x_lim
        self.Eq = Eq
        self.n = 10000
        self.h = (self.x_lim-self.xo)/self.n
        self.y1 = [self.yo]
        for i in range(self.n):
            y2 = self.y1[i]+self.h*f(self.xo+i*self.h,self.y1[i],self.Eq)
            self.y1.append(y2)
    def plot_emd(self):
        y = np.array(self.y1)
        x = np.linspace(self.xo,self.x_lim,np.size(y))
        plt.plot(x,y,linestyle = "solid")
        plt.savefig("Images/EMethod.png",bbox_inches='tight')
        plt.clf()
def f(x,y,eq):
    f = eval(eq)
    return f
