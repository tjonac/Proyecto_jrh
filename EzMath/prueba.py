import tkinter
from tkinter import PhotoImage
from PIL import Image,ImageTk
root = tkinter.Tk()  
root.geometry("960x600")
img = Image.open("EzMath/Images/mate.png")
img = img.resize((500, 250), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
botonNuevo1 = tkinter.Button(root, image=img, text="click aqui", compound="top")
botonNuevo1.place(x=500, y=100)
botonNuevo1.pack() 

root.mainloop()