from tkinter import *


def incrementar():
     valor= int(etiqValor["text"])
     etiqValor["text"]= f"{valor+1}"

def restar():
     valor= int(etiqValor["text"])
     etiqValor["text"]= f"{valor-1}"

def reset():
     valor= int(etiqValor["text"])
     etiqValor["text"]= 0

window=Tk()
window.title("Contador")
window.geometry('300x200')
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
window.minsize(400, 150) 
window.maxsize(400, 150)
window.configure(background= 'dark turquoise')


etiqCont=Label(window,text= "Contador ",font= "arial",relief=RIDGE)
etiqCont.place( x=30,y=60)
etiqValor=Label(window, text=" 0", font="arial",relief= RIDGE)
etiqValor.place(x=120,y=60)

botonIncrementar= Button(window, text= "Count Up",command=incrementar,bg="#ABEBC6")
botonIncrementar.place(x=30,y=120)
botonRestar= Button(window, text= "Count Down",command=restar,bg="#F9E79F")
botonRestar.place(x=110,y=120 )
botonReset= Button(window, text= "Reset",command=reset,bg="pink")
botonReset.place(x=150,y= 60)

window.mainloop()
