"""
Programa principal donde se ejecuta el GUI
"""
#Importaciones
from os import X_OK
import tkinter as tk
from tkinter import DoubleVar, PhotoImage, StringVar, Toplevel,ttk
from tkinter import font
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import text
import numpy as np
import Dx 
import EulerMethod as emd
import Int 
import Graficador as gph
#<------------------------------Funciones---------------------------->
def math_window():

    def euler_window():
        def finish():                                                                                         #Se ejecuta al presionar el botón "Aceptar"
            grafica = emd.euler_method(float(x0.get()),float(y0.get()),float(x_lim.get()),str(ec.get()))      #Se llama a la clase con los arguementos necesarios del programa EulerMethod.py
            grafica.plot_emd()                                                                                #Se genera la grafica con el metodo del programa EulerMethod.py
            grafica_image = tk.PhotoImage(file="Images/EMethod.png")                                   #Se cambia  la imagen
            grafica_label = tk.Label(euler,image=grafica_image).place(x=100,y=300)                            #Se inserta la nueva imagen 
            grafica_label.image = grafica_image                                                               #Python elimina las variables locales (las definidas en funciones) como limpiador de basura, esto lo evita

        math_root.destroy()     #Se cierra la ventana de mate
        #<----------------------Configuración nueva ventana--------------------->
        euler = tk.Toplevel(root)
        euler.title("EzMath")
        euler.geometry("800x1000")
        #<---------------------------Líneas de texto---------------------------->
        label1 = tk.Label(euler,text="Este programa grafica la solución a ecuaciones diferenciales de la forma: ")
        label1.pack(anchor=tk.CENTER)
        label1.config(fg="black",font=("Arial",24))

        label2 = tk.Label(euler,text="y'=F(x,y)")
        label2.pack(anchor=tk.CENTER)
        label2.config(fg="black",font=("Cambria Math",24))

        label3 = tk.Label(euler,text="Ingrese la ecuación en sintaxis de python y numpy como np: ")
        label3.place(x=50,y=100)

        label4 = tk.Label(euler, text="Ingrese la coordenada x de la condición inicial:")
        label4.place(x=50,y=150)

        label5 = tk.Label(euler, text="Ingrese la coordenada y de la condición incial:")
        label5.place(x=50,y=200)

        label6 = tk.Label(euler,text="Ingrese el valor de x hasta donde desee graficar: ")
        label6.place(x=50,y=250)
        #<------------------------------Entradas--------------------------------->
        ec = StringVar()
        ttk.Entry(euler,textvariable=ec).place(x=500,y=100)

        x0 = DoubleVar()
        ttk.Entry(euler,textvariable=x0).place(x=500,y=150)

        y0 = DoubleVar()
        ttk.Entry(euler,textvariable=y0).place(x=500,y=200)

        x_lim = DoubleVar()
        ttk.Entry(euler,textvariable=x_lim).place(x=500,y=250)
        #<-------------------------------Botones--------------------------------->
        tk.Button(euler,text="Aceptar",command=finish).place(x=400,y=270)
        #<-------------------------------Imagenes-------------------------------->
        grafica_image = tk.PhotoImage(file="Images/Base.png")                    #Se procesa la imagen 
        grafica_label = tk.Label(euler,image=grafica_image).place(x=80,y=300)           #Se inserta la imagen
        grafica_label.image = grafica_image

    def derivative_window():
        def finish():
            #<----------------Se introducen los datos en la función-------------->
            s = Dx.derivative(float(a.get()),str(ec.get()))
            s.plot_dx()                                         #Se hace la grafica

            resultado = StringVar()
            resultado.set(str(s.result_dx()))
            tk.Label(dx_ventana,text=resultado.get(),fg="black",font=("Arial",14)).place(x=300,y=250)

            grafica_image = tk.PhotoImage(file="Images/Derivada.png")        #Se cambia  la imagen
            grafica_label = tk.Label(dx_ventana,image=grafica_image).place(x=65,y=266)
            grafica_label.image = grafica_image


        math_root.destroy()
        #<------------------Configuración de ventana------------------>
        dx_ventana = tk.Toplevel(root)
        dx_ventana.title("EzMath")
        dx_ventana.geometry("800x850")
        #<--------------------Líneas de texto------------------------->
        label1 = tk.Label(dx_ventana,text="Este programa da el valor de la derivada en un punto dado y su grafica ")
        label1.pack(anchor=tk.CENTER)
        label1.config(fg="black",font=("Arial",24))

        tk.Label(dx_ventana,text="Ingrese la ecuación en sintaxis de python y numpy como np: ",fg="black",font=("Arial",14)).place(x=50,y=100)

        tk.Label(dx_ventana, text="Ingrese el punto donde desea conocer la derivada",fg="black",font=("Arial",14)).place(x=50,y=150)

        tk.Label(dx_ventana,text="El valor de la derivada es: ",fg="black",font=("Arial",14)).place(x=50,y=250)
        #<-----------------------Entradas----------------------------->
        ec = StringVar()
        ttk.Entry(dx_ventana,textvariable=ec).place(x=500,y=100)
        a = DoubleVar()
        ttk.Entry(dx_ventana,textvariable=a).place(x=500,y=150)
        #<-----------------------Botones------------------------------->
        tk.Button(dx_ventana,text="Aceptar",command=finish).place(x=400,y=200)

        grafica_image = tk.PhotoImage(file="Images/Base.png")                    #Se procesa la imagen 
        grafica_label = tk.Label(dx_ventana,image=grafica_image).place(x=80,y=300)           #Se inserta la imagen
        grafica_label.image = grafica_image

    def integrate_window():
        def finish():
            #<----------------Se introducen los datos en la función-------------->
            s = Int.integrate(float(a.get()),float(b.get()),str(ec.get()))
            s.plot_int()                                                    #Se hace la grafica

            resultado = StringVar()
            resultado.set(str(s.result_int()))
            resultado_label = tk.Label(int_ventana,text=resultado.get(),fg="black",font=("Arial",14))
            resultado_label.place(x=300,y=250)

            grafica_image = tk.PhotoImage(file="Images/Integral.png")           #Se cambia  la imagen
            grafica_label = tk.Label(int_ventana,image=grafica_image).place(x=65,y=290)
            grafica_label.image = grafica_image


        math_root.destroy()
        #<-----------------Configuración de ventana------------------->
        int_ventana = tk.Toplevel(root)
        int_ventana.title("EzMath")
        int_ventana.geometry("800x900")
        #<--------------------Líneas de texto------------------------->
        label1 = tk.Label(int_ventana,text="Este programa da el valor de la integral desde a hasta b de f(x)")
        label1.pack(anchor=tk.CENTER)
        label1.config(fg="black",font=("Arial",24))

        tk.Label(int_ventana,text="Ingrese la ecuación en sintaxis de python y numpy como np: ",fg="black",font=("Arial",14)).place(x=50,y=50)

        tk.Label(int_ventana, text="Ingrese el valor de a: ",fg="black",font=("Arial",14)).place(x=50,y=100)

        tk.Label(int_ventana,text="Ingrese el valor de b: ",fg="black",font=("Arial",14)).place(x=50,y=150)

        tk.Label(int_ventana,text="El valor de la integral es: ",fg="black",font=("Arial",14)).place(x=50,y=250)
        #<-----------------------Entradas----------------------------->
        ec = StringVar()
        ttk.Entry(int_ventana,textvariable=ec).place(x=500,y=50)
        a = DoubleVar()
        ttk.Entry(int_ventana,textvariable=a).place(x=500,y=100)
        b = DoubleVar()
        ttk.Entry(int_ventana,textvariable=b).place(x=500,y=150)
        #<-----------------------Botones------------------------------->
        tk.Button(int_ventana,text="Aceptar",command=finish).place(x=400,y=200)

        grafica_image = tk.PhotoImage(file="Images/Base.png")                    #Se procesa la imagen 
        grafica_label = tk.Label(int_ventana,image=grafica_image).place(x=80,y=350)           #Se inserta la imagen
        grafica_label.image = grafica_image

    def plotter():
        def plotter_peq():                                  #peq = Parametric EQuations
            def finish():
                s = gph.parametric(float(t_lim1.get()),float(t_lim2.get()),str(x_eq.get()),str(y_eq.get()))
                s.plot_peq()      #Se hace la grafica

                grafica_image = tk.PhotoImage(file="Images/ParametricEq.png")       #Se cambia  la imagen
                grafica_label = tk.Label(peq_ventana,image=grafica_image).place(x=65,y=280)
                grafica_label.image = grafica_image
   
            graficador_ventana.destroy()

            peq_ventana = tk.Toplevel(root)                 #Crea la nueva ventana
            peq_ventana.title("EzMath")                     #Titulo de la nueva ventana
            peq_ventana.geometry("800x850")                 #Tamaño de la nueva ventana

            tk.Label(peq_ventana,text="Se graficará la curva descrita por las ecuaciones parametricas",fg="black",font=("Arial",14)).pack(anchor=tk.CENTER)
            tk.Label(peq_ventana,text="Ingrese el valor incial de t:",fg="black",font=("Arial",14)).place(x=50,y=50)
            tk.Label(peq_ventana,text="Ingrese el valor final de t:",fg="black",font=("Arial",14)).place(x=50,y=100)
            tk.Label(peq_ventana,text="Ingrese la ecuación x=f(t):",fg="black",font=("Arial",14)).place(x=50,y=150)
            tk.Label(peq_ventana,text="Ingrese la ecuación y=g(t):",fg="black",font=("Arial",14)).place(x=50,y=200)

            t_lim1 = DoubleVar()
            ttk.Entry(peq_ventana,textvariable=t_lim1).place(x=300,y=50)
            t_lim2 = DoubleVar()
            ttk.Entry(peq_ventana,textvariable=t_lim2).place(x=300,y=100)
            x_eq = StringVar()
            ttk.Entry(peq_ventana,textvariable=x_eq).place(x=300,y=150)
            y_eq = StringVar()
            ttk.Entry(peq_ventana,textvariable=y_eq).place(x=300,y=200)

            tk.Button(peq_ventana,text="Aceptar",command=finish).place(x=400,y=250)

            grafica_image = tk.PhotoImage(file="Images/Base.png")                    #Se procesa la imagen 
            grafica_label = tk.Label(peq_ventana,image=grafica_image).place(x=80,y=300)           #Se inserta la imagen
            grafica_label.image = grafica_image

        def plotter_eq_2d():
            def finish():
                s = gph.graphic_2d(float(x_lim1.get()),float(x_lim2.get()),str(eq.get()))
                s.plot_eq2d()      #Se hace la grafica

                grafica_image = tk.PhotoImage(file="Images/Eq_2d.png")       #Se cambia  la imagen
                grafica_label = tk.Label(eq2d_ventana,image=grafica_image).place(x=65,y=280)
                grafica_label.image = grafica_image
   
            graficador_ventana.destroy()

            eq2d_ventana = tk.Toplevel(root)                 #Crea la nueva ventana
            eq2d_ventana.title("EzMath")                     #Titulo de la nueva ventana
            eq2d_ventana.geometry("800x850")                 #Tamaño de la nueva ventana

            tk.Label(eq2d_ventana,text="Se graficará la función y=f(x)",fg="black",font=("Arial",16)).pack(anchor=tk.CENTER)
            tk.Label(eq2d_ventana,text="Ingrese el valor incial de x:",fg="black",font=("Arial",14)).place(x=50,y=50)
            tk.Label(eq2d_ventana,text="Ingrese el valor final de x:",fg="black",font=("Arial",14)).place(x=50,y=100)
            tk.Label(eq2d_ventana,text="Ingrese la ecuación y=f(x):",fg="black",font=("Arial",14)).place(x=50,y=150)

            x_lim1 = DoubleVar()
            ttk.Entry(eq2d_ventana,textvariable=x_lim1).place(x=300,y=50)
            x_lim2 = DoubleVar()
            ttk.Entry(eq2d_ventana,textvariable=x_lim2).place(x=300,y=100)
            eq = StringVar()
            ttk.Entry(eq2d_ventana,textvariable=eq).place(x=300,y=150)

            tk.Button(eq2d_ventana,text="Aceptar",command=finish).place(x=400,y=200)

            grafica_image = tk.PhotoImage(file="Images/Base.png")                    #Se procesa la imagen 
            grafica_label = tk.Label(eq2d_ventana,image=grafica_image).place(x=80,y=250)           #Se inserta la imagen
            grafica_label.image = grafica_image


        math_root.destroy()

        graficador_ventana = tk.Toplevel(root)                 #Crea la nueva ventana
        graficador_ventana.title("EzMath")                     #Titulo de la nueva ventana
        graficador_ventana.geometry("800x550")                 #Tamaño de la nueva ventana

        tk.Label(graficador_ventana,text="¿Qué deseas graficar?",bg="black",font=("Arial",28)).pack(anchor=tk.CENTER)
        
        tk.Button(graficador_ventana,text="Función y=f(x)",command=plotter_eq_2d).place(x=50,y=100)
        tk.Button(graficador_ventana,text="Ecuaciones Parametricas",command=plotter_peq).place(x=50,y=150)
        tk.Button(graficador_ventana,text="Vectores R^2").place(x=50,y=200)

    #<----------------------Configuración de ventana------------------>
    root.iconify()                                #Miniminiza root 
    math_root = tk.Toplevel(root)                 #Crea la nueva ventana
    math_root.title("EzMath")                     #Titulo de la nueva ventana
    math_root.geometry("800x550")                 #Tamaño de la nueva ventana
    #<---------------------------Imagenes----------------------------->
    tk.Label(math_root,image=p2).place(x=200,y=50) #Se inserta la imagen
    #----------------------------Botones------------------------------>
    tk.Button(math_root,text="Método de Euler",command=euler_window).place(x=50,y=200)          #Botón Metodo de Euler
    tk.Button(math_root,text="Derivación Numérica",command=derivative_window).place(x=50,y=250) #Botón Deivación Numérica
    tk.Button(math_root,text="Integración Numérica",command=integrate_window).place(x=50,y=300) #Botón Integración Numérica
    tk.Button(math_root,text="Graficador",command=plotter).place(x=50,y=350)
    

def physics_window():
    root.iconify()
    physics_root = Toplevel(root)
    physics_root.title("EzMath")
    physics_root.geometry("800x550")


#<-----------Configuración de la ventana principal root---------->
root = tk.Tk()
root.title("EzMath")
root.geometry("800x550")
root.iconbitmap("Images/icon.ico")
root.config(bg="white")
#<--------------------------Imagenes----------------------------->
Logo = tk.PhotoImage(file="Images/Logo.png")  #Se procesa la imagen
tk.Label(root,image=Logo).place(x=200,y=0)           #Se inserta la imagen

p1 = tk.PhotoImage(file="Images/P1.png")      #Se procesa la imagen 
tk.Label(root,image=p1).place(x=150,y=200)           #Se inserta la imagen

p2 = tk.PhotoImage(file="Images/P2.png")      #Se procesa la imagen (Lo demás en función)

mate = Image.open("Images/mate.jpg")     #Se procesa la imagen 
mate = mate.resize((250, 150), Image.ANTIALIAS) #Redimension (Alto, Ancho)
mate = ImageTk.PhotoImage(mate)                 #Se inserta la imagen

#<----------------------------Botones----------------------------->
tk.Button(root, image=mate, text="Presiona aqui", compound="top",command=math_window).place(x=250,y=300)




root.mainloop() #Hace un ciclo infinito para que el programa no se cierre

