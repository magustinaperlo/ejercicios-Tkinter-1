from tkinter import *
from tkinter import messagebox

def validar():
    try:
        valor1=num1.get()
        valor2 = num2.get()
    except:
        messagebox.showwarning("Error","Debe ingresar dos valores numericos")

def borrar():
    num1.set("")
    num2.set("")


def operaciones():
    validar()
    n1= num1.get()
    n2= num2.get()
    op= opcion.get()
    if op==1:
        res.set(n1+n2)
        borrar()
    if op==2:
        res.set(n1-n2)
        borrar()
    if op==3:
        res.set(n1*n2)
        borrar()
    if op==4:
        if int(num2.get())!=0:
            res.set(n1/n2)
            borrar()
        else:
         messagebox.showerror ("Error", "No es posible dividir por 0,ingrese otro número")
      



window= Tk()
num1 = IntVar()
num2 = IntVar()
res = IntVar()
opcion = IntVar()
window.geometry('400x300')
window.configure(bg="burlywood")
window.title("Calculadora con RadioButton")

lbNumero1=Label(window, text= "Valor 1 : ",font="arial",bg="gold")
lbNumero1.place(x=10,y=50)
lbNumero2=Label(window, text= "Valor 2 : ",font="arial",bg="gold")
lbNumero2.place(x=10,y=90)
lbResultado= Label(window,text="Resultado",font="arial",bg= "gold")
lbResultado.place(x=10 , y=150 )
lbRes= Label(window,bg= "white",textvariable= res)
lbRes.place(x=100,y=150 )
lbOperaciones=Label(window, text="Operaciones",font="arial,13",bg="burlywood")
lbOperaciones.place(x=280,y=20)

numero1 = Entry (window,textvariable= num1)
numero1.place(x=100,y= 50)
numero2= Entry (window,textvariable= num2)
numero2.place(x=100,y= 90)

botCalcular= Button(window, text= "Calcular",bg="coral",relief= RAISED, command= operaciones)
botCalcular.place(x=80,y= 200 )

radioSuma= Radiobutton( window, text= "Suma ", value=1, variable=opcion,bg="burlywood")
radioSuma.place(x=280,y= 60 )
radioResta= Radiobutton( window, text= "Resta ", value=2, variable=opcion,bg="burlywood")
radioResta.place(x=280,y= 90 )
radioMultiplicar= Radiobutton( window, text= "Multiplicar ", value=3, variable=opcion,bg="burlywood")
radioMultiplicar.place(x=280,y= 120 )
radioDividir= Radiobutton( window, text= "Dividir ", value=4, variable=opcion,bg="burlywood")
radioDividir.place(x=280,y= 150 )





window.mainloop()