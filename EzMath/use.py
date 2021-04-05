from Dx import *
from EulerMethod import *
from Int import *

#Integral de -1 a 1 de media circunferencia unitaria):
p1 = integrate(-1,1,"np.sqrt(1-x**2)")
p1.plot_int()
print(p1.result_int())
#Su valor real es de pi/2

#Derivar sin(x) en x = pi
p2 = derivative(3.1416,"np.sin(x)")
p2.plot_dx()
print(p2.result_dx())

#Su valor real es de -1

#Grafica de y tal que: y'=2*x con y(0)=0, grafica desde x=0 hasta x = 2
p3 = euler_method(0,0,2,"2*x")
p3.graph()
#Ecuación de x^2