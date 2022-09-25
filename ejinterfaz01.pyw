from cProfile import label
from tkinter import *
def incrementar():
    valor=int(lineEdit["text"])
    lineEdit["text"]= f"{valor+1}"
window = Tk() 
window.title("Cont. Creciente")
window.geometry('500x200')
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
window.minsize(500, 150) 
window.maxsize(500, 150)
etiqueta= Label (window, width= 15, text= "Contador")
etiqueta.grid(row=0, column=0)
lineEdit= Label( window,text= "0", width= 15, bg= "white")
lineEdit.grid( row=0 , column=1)
botonIncrementar= Button( window, width=15, text= "+", command= incrementar)
botonIncrementar.grid( row= 0, column=3)

window.mainloop()
