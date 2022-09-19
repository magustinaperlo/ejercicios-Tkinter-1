from faulthandler import disable
from tkinter import *
from tkinter import messagebox

def validar():
    try:
        valor1=num1.get()
        valor2 = num2.get()
    except:
        messagebox.showwarning("Error","Debe ingresar dos valores numericos")

window =Tk()
num1= IntVar()
num2= IntVar()
resultado= IntVar()

def sumar():
    validar()
    resultado.set( float(num1.get()) + float(num2.get()) )
    borrar()

def resta():
    validar()
    resultado.set( float(num1.get()) - float(num2.get()) )
    borrar()

def multiplicar():
    validar()
    resultado.set( float(num1.get()) * float(num2.get()) )
    borrar()

def dividir():
    validar()
    if int(num2.get())!=0:
            resultado.set(float(num1.get()) / float( num2.get()))
            validar()
    else:
         messagebox.showerror ("Error", "No es posible dividir por 0,ingrese otro número")
    borrar()

def porcentaje():
    resultado.set( float(num1.get()) * float(num2.get() / 100) )
    borrar()

def borrar():
    num1.set("")
    num2.set("")

def clear():
    num1.set("")
    num2.set("")
    resultado.set("")

window.title("Calculadora")
window.geometry ('300x300')
window.configure(background= "#FCF3CF",cursor= "heart")

etiqueta1=Label(window, text="Numero 1",background="white",relief="ridge")
etiqueta1.place (x=10, y=40)
etiqueta2=Label(window, text="Numero 2", background= "white",relief="ridge")
etiqueta2.place (x=10, y=90)
etiquetaResultado=Label(window, text="Resultado: ", background= "white",relief="ridge")
etiquetaResultado.place (x=10, y=150)
botonSuma=Button(window, text="  +  ",background="white",command=sumar)
botonSuma.place (x=10, y=200)
botonResta=Button(window, text="  -  ",background="white",command=resta)
botonResta.place (x=50, y=200)
botonMultiplicar=Button(window, text="  x  ",background="white",command=multiplicar)
botonMultiplicar.place (x=80, y=200)
botonDividir=Button(window, text="  /  ",background="white",command=dividir)
botonDividir.place (x=110, y=200)
botonPorcentaje=Button(window, text="  %  ",background="white", command= porcentaje)
botonPorcentaje.place (x=140, y=200)
botonClear=Button(window, text=" Clear ",background="white",command=clear)
botonClear.place (x=10, y=230)

caja1= Entry( window, textvariable= num1)
caja1.place( x=100, y= 40)
caja2= Entry( window, textvariable= num2)
caja2.place( x=100, y= 90)
cajaResultado=Entry ( window, textvariable=resultado, state= "readonly")
cajaResultado.place( x=100, y= 150)
window.mainloop()