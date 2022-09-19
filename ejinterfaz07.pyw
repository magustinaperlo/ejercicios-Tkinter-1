from cgitb import text
from tkinter import *
from random import *

def GenerarNumero():

    if int(numVariable1.get()) > int(numVariable2.get()):
        nroRandom=str(randint(int(numVariable2.get()), int(numVariable1.get())))
        NumGenerado.set(nroRandom)
    elif int(numVariable1.get()) < int(numVariable2.get()):
        nroRandom=str(randint(int(numVariable1.get()), int(numVariable2.get())))
        NumGenerado.set(nroRandom)

window=Tk()
window.title("Generador de Numeros")
window.configure(bg= "pink", cursor= "hand1")
window.geometry('500x300')

Numero1=Label(window,bg="pink", text="Numero 1 :")
Numero1.place(x=80,y=50)
Numero2=Label(window,bg="pink", text="Numero 2 :")
Numero2.place(x=80,y=120)

numVariable1= StringVar()
numVariable2= StringVar()

box1= Spinbox(window, from_= 0 , to_= 5000, textvariable= numVariable1)
box1.place(x=230,y=50 )

box2= Spinbox(window, from_= 0 , to_= 5000, textvariable= numVariable2)
box2.place(x=230,y=120 )

EtiquetaNumeroGenerado=Label(window, text="Numero Generado :", bg="pink")
EtiquetaNumeroGenerado.place(x= 80,y= 170)

NumGenerado=StringVar()
NumeroGenerado=Label( window,textvariable= NumGenerado, width= 18 )
NumeroGenerado.place(x=230,y=170)

BotonGenerar= Button( window, text= "Generar", command= GenerarNumero ,borderwidth= 5)
BotonGenerar.place(x=260,y=230)





window.mainloop()

