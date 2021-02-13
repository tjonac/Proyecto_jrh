"""
Este programa grafica la función dada por el array "y", además rellena el área
entre la curva y el eje x.
"""
#--------------Importaciones---------------
import numpy as np         
import matplotlib.pyplot as plt
#--------------Declaraciones---------------
v_i = -np.pi #valor inicial donde empieza el vector x
v_f = np.pi  #valor final del vector x 
h   = 0.01   #Salto entre cada valor

lblue = "#90e0ef" #Color en rgb, si quieres encontrar más en este formato, visita:
#https://coolors.co/palettes/trending

#Para graficar se crea un arreglo 1xn "x" donde el primer elemento es v_i, cada
#valor se consigue sumandole al anterior h, el valor final es (v_f)-h 
#Después se crea el arreglo "y" 1xn el cual debe de ser del mismo tamaño que x, 
#al usarlo en la función, este se hace en automatico del mismo tamaño. La función
#plt.plot grafica cada par ordenado (x,y) y los une por medio de lineas, por lo tanto
#entre mayor sea el número de elementos en x,y será más smooth
x = np.arange(v_i,v_f,h) 
y = np.sin(x)

#-----------------Grafica---------------------

plt.plot(x,y, color="blue") 
plt.xlabel("Eje x")    #Leyenda del eje x
plt.ylabel("Eje y")    #Leyenda del eje y
plt.title("$\sin{x}$") #Titulo de la grafica
plt.fill_between(x,y, color=lblue) #Se rellena el área
plt.show()             #Esto hace qu eal compilarlo se muestre la grafica.