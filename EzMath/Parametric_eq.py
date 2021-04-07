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


