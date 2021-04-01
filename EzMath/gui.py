"""
Programa principal donde se ejecuta el GUI
"""
#Importaciones
import tkinter as tk
from tkinter import PhotoImage, Toplevel
from PIL import Image,ImageTk

#Funciones
def math_window():
    root.iconify()
    math_root = tk.Toplevel(root)
    math_root.title("EzMath")
    math_root.geometry("800x550")
    #Imagenes
    p2 = tk.PhotoImage(file="EzMath/Images/P2.png")
    tk.Label(math_root,image=p2).place(x=150,y=0)
    #Botones
    tk.Button(math_root,text="Método de Euler").place(x=50,y=200)
    tk.Button(math_root,text="Derivación Numérica").place(x=50,y=250)
    tk.Button(math_root,text="Integración Númerica").place(x=50,y=300)





def physics_window():
    root.iconify()
    physics_root = Toplevel(root)
    physics_root.title("EzMath")
    physics_root.geometry("800x550")

#Configuración de la ventana principal root
root = tk.Tk()
root.title("EzMath")
root.geometry("800x550")
root.iconbitmap("EzMath/Images/icon.ico")
root.config(bg="white")
#Imagenes
Logo = tk.PhotoImage(file="EzMath/Images/Logo.png")
tk.Label(root,image=Logo).place(x=200,y=0)

p1 = tk.PhotoImage(file="EzMath/Images/P1.png")
tk.Label(root,image=p1).place(x=150,y=200)

mate = Image.open("EzMath/Images/mate.jpg")
mate = mate.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
mate = ImageTk.PhotoImage(mate)

fisica = Image.open("EzMath/Images/fisica.jpg")
fisica = fisica.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
fisica = ImageTk.PhotoImage(fisica)

#Botones
botonMate = tk.Button(root, image=mate, text="Presiona aqui", compound="top",command=math_window)
botonMate.place(x=100,y=300)

botonFisica = tk.Button(root,image=fisica,text="Presiona aqui",compound="top",command=physics_window)
botonFisica.place(x=450,y=300)


root.mainloop()

