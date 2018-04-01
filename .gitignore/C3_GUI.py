from Tkinter import *

root = Tk()
root.title("Circuitos 3")
root.geometry('400x400')


## FUNCIONES ##

def dato_recibido():
	d_temp = d_enviar.get()
	d_display=Text(master=root, height=2, width=4)
	d_display.grid(column=1, row=4)
	d_display.insert(INSERT,d_temp)


## LABELS ##
## Titulo ##
title = Label(text="Control Motor",font='Helvetica 18 bold', fg="blue")
title.grid(column = 1, row=0)
## Label para enviar ##
l_enviar = Label(text="Escribe el caracter:")
l_enviar.grid(column=0, row=1)

l_recibir = Label(text="Recibiendo datos:")
l_recibir.grid(column=0, row=4)

## Botones ##
## boton para enviar ##
b_enviar = Button(text="ENVIAR", fg="green", command = dato_recibido, width="10")
b_enviar.grid(column=0, row=2)


## Entradas ##
d_enviar = Entry()
d_enviar.grid(column=1, row=1)



root.mainloop()









