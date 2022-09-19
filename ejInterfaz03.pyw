import math
from tkinter import *
 
def calcularFact():      
    calculo = int(numero.get())+1
    EtiquetaResultado.config(text= math.factorial(calculo))
    for i in range(calculo):
        numero.set(calculo)
   

ventana = Tk()   
ventana.title("Factorial") 
ventana.geometry('600x370') 
ventana.resizable(width=False,height=False)
ventana.rowconfigure([0,1,2], minsize = 50, weight= 1)
ventana.columnconfigure([0,1,2,3],minsize = 50, weight= 1 )
ventana.config(bg="lavender")

etiquetaN = Label(ventana,width = 15,relief="ridge",text = "n: ", font= ("Arial",11), bg = "aquamarine")
etiquetaN.grid(row=0,column =0 )

numero=IntVar(value=0)                                                   
NumInicial = Entry(ventana,width=15,justify = "center", textvariable=numero,state= "readonly",font= ("Arial",11),bg = "white")
NumInicial.grid (row=0,column = 1, padx=7,pady=7, ipady = 10)

etiquetaFactorial = Label(ventana,width = 15,relief="ridge",text = " Factorial de n: ",font= ("Arial",11), bg ="aquamarine" )
etiquetaFactorial.grid(row=1,column =0 )

EtiquetaResultado=Label(ventana,text="1", width = 20, font= ("Arial",12),bg = "white" )
EtiquetaResultado.grid(row=1,column=1, padx=7,pady=7,ipady = 10)

boton = Button(ventana, width = 10, text = "Siguiente ", font= ("Arial",11), command= calcularFact, bg = "SlateBlue1")
boton.grid (row=2, column=1)

ventana.mainloop()