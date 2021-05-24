"""
Este programa grafica curvas descritas por ecuaciones parametricas.
"""
import numpy as np
import matplotlib.pyplot as plt 

#<---------------------------Funciones---------------------------->
def f(t,x_eq):
    f = eval(x_eq)
    return f

def g(t,y_eq):
    g = eval(y_eq)
    return g

def h(x,eq):
    h = eval(eq)
    return h

class parametric():
    def __init__(self,t_lim1,t_lim2,x_eq,y_eq):
        self.t_lim1 = t_lim1
        self.t_lim2 = t_lim2
        self.x_eq  = x_eq
        self.y_eq = y_eq

    def plot_peq(self):
        t = np.arange(self.t_lim1,self.t_lim2,0.01)
        x = f(t,self.x_eq)
        y = g(t,self.y_eq)

        plt.plot(x,y,color="#023e8a")
        plt.savefig("EzMath/Images/ParametricEq.png")
        plt.clf()

class graphic_2d():
    def __init__(self,x_lim1,x_lim2,eq):
        self.x_lim1 = x_lim1
        self.x_lim2 = x_lim2
        self.eq = eq
    def plot_eq2d(self):
        x = np.arange(self.x_lim1,self.x_lim1,0.01)
        y = h(x,self.eq)
        plt.plot(x,y, color="#023e8a")
        plt.savefig("EzMath/Images/Eq_2d.png")
        plt.clf()

