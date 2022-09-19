from cProfile import label
from tkinter import *
def incrementar():
    valor=int(lineEdit["text"])
    lineEdit["text"]= f"{valor+1}"
window = Tk() 
window.title("Cont. Creciente")
window.geometry('300x200')
etiqueta= Label (window, width= 15, text= "Contador")
etiqueta.grid(row=0, column=0)
lineEdit= Label( window,text= "0", width= 15, bg= "white")
lineEdit.grid( row=0 , column=1)
botonIncrementar= Button( window, width=15, text= "+", command= incrementar)
botonIncrementar.grid( row= 0, column=3)

window.mainloop()