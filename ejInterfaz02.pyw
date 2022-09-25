from cProfile import label
from tkinter import *
def restar():
    valor=int(lineEdit["text"])
    lineEdit["text"]= f"{valor-1}"
window = Tk()
window.title("Cont. Decreciente")
window.geometry('400x100')
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
window.minsize(400, 100) 
window.maxsize(400, 100)
etiqueta= Label (window, width= 15, text= "Contador")
etiqueta.grid(row=0, column=0)
lineEdit= Label( window, text= "88", width= 15, bg= "white")
lineEdit.grid( row=0 , column=1)
botonRestar= Button( window, width=15, text= "-", command= restar)
botonRestar.grid( row= 0, column=3)

window.mainloop()
