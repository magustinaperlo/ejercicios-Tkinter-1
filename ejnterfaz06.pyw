from tkinter import *
from tkinter import messagebox

def añadir():
#     PeliculaIngresadas.insert(END, ingresoPelicula.get())
#     ingresoPelicula.delete(0,END)
# debemos validar que ingrese sin espacios en la primer posicion o en su defecto una cadena VACIA
     a = ingresoPelicula.get()
    # entrada=input()
     if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
     else:
        PeliculaIngresadas.insert(END,a)
        ingresoPelicula.delete(0,END)
    
ventana=Tk()
ventana.geometry("500x300")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("Peliculas")
ventana.config(bg="cyan")

NombrePelicula=Label(ventana, text="Ingrese el título de una película : ", bg="light cyan", font="Palatino, 11")
NombrePelicula.place(x=15, y=32)

ListaPeliculas=Label(ventana, text="PELICULAS", bg="medium turquoise", font="Palatino")
ListaPeliculas.place(x=318, y=30)

ingresoPelicula=Entry(ventana, bg="white", bd=3, font="verdana, 11")
ingresoPelicula.place(x=26, y=80, width=180, height=30)

botonAñadir=Button(ventana, text="Añadir ", font="Palatino, 11", bg="medium spring green", bd=3, command=añadir)
botonAñadir.place(x=90, y=130)

PeliculaIngresadas=Listbox(ventana, bg="white", bd=2, font="verdana, 11")
PeliculaIngresadas.place (x=250, y=60, width=210)


ventana.mainloop()
