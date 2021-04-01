from Dx import *
from EulerMethod import *
from Int import *

#Integral de 0 a infinito e**(-x**2):
p1 = integrate(0,1000,"np.exp(-x**2)")
print(p1.I())
#Su valor real es de sqrt(pi)/2, que es aprox 0.886226925

#Derivar sin(x) en x = pi
p2 = derivative(np.pi,"np.sin(x)")
print(p2.derivate())
#Su valor real es de -1

#Grafica de y tal que: y'=-x/y con y(-1)=0.1 (y'no está definida cuando y=0), grafica desde x=-1 hasta x = 1
p3 = euler_method(-1,0.1,1,"-x/y")
p3.graph()
#Ecuación diferencial de circunferencia unitaria