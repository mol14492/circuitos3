from Tkinter import *
import ttk
import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import serial as SR
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import ttk
import Tkinter
from drawnow import *
import matplotlib.animation as animation
import sys

class App:
    ser = 0
    def __init__(self, master):
        def plot_graph():
            grafica.plot(values)

        def animate(i):
            d_temp = ser.readline()
            if d_temp==b'':
                d_temp=chr(0)
            else:
                d_temp=d_temp
            d_temp_int = ord(d_temp)
            values.append(d_temp_int)
            drawnow(plot_graph)
            plt.pause(.000001)         
        ## VARIABLES ##
        values=[]
        global variable
        global variable2
        #global variable3
        global grafica
        variable2 = StringVar()
        variable = StringVar()
        ## SERIAL ##
        global ser          #Must be declared in Each Function
        ser = SR.Serial()
        ser.baudrate = 9600
        ser.port = 'COM7'
        ser.timeout = 0.5
        ser.open()          #Opens SerialPort
        # print port open or closed
        if ser.isOpen():
            print ('Open: ' + ser.portstr)
        #Creamos un frame
        frame = Tkinter.Frame(master)
        ## LABELS ##
        ## Titulo1 ##
        self.title = Label(text="Control Motor",font='Helvetica 18 bold', fg="blue")
        self.title.grid(column = 1, row=0)
        ## Titulo2 ##
        self.title = Label(text=" Tiempo",font='Helvetica 12 bold', fg="black")
        self.title.grid(column = 4, row=3)
        ## Titulo3 ##
        self.title = Label(text=" Velocidad",font='Helvetica 12 bold', fg="black")
        self.title.grid(column = 1, row=6)
        ## Titulo3 ##
        self.title = Label(text=" Grafico",font='Helvetica 18 bold', fg="blue")
        self.title.grid(column = 4, row=1) 
        ## BOTONES ##
        ## boton para enviar ##
        self.b_enviar = Button(text="ENVIAR",command = self.dato_enviar, width="10")
        self.b_enviar.grid(column=1, row=2)
        self.b_salir = Button(text="SALIR",command = self.salir, width="10")
        self.b_salir.grid(column=0, row=8)
        self.b_disminuir = Button(text="<<DISMINUIR",command = self.disminuir_velocidad, width="12")
        self.b_disminuir.grid(column=1, row=7)
        self.b_aumentar = Button(text="AUMENTAR>>",command = self.aumentar_velocidad, width="12")
        self.b_aumentar.grid(column=2, row=7)
        ## GRAFICA ## (FALTA AGREGAR COSOS)
        figura = Figure(figsize=(5,4))
        grafica = figura.add_subplot(111)
        plt.ion()##
        #Dibujar Grafica#
        self.canvas = FigureCanvasTkAgg(figura,master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=4, row=6)
        self.animacion = animation.FuncAnimation(figura,animate,interval=0.1)
        ## Label para enviar ##
        self.l_enviar = Label(text="Escribe el caracter:")
        self.l_enviar.grid(column=0, row=1)
        ## Label para Velocidad ##
        self.l_control = Label(text="Control Velocidad:")
        self.l_control.grid(column=0, row=7)
        ## COMBO ##
        self.box = ttk.Combobox(root, textvariable=variable)
        self.box['values'] = ('A', 'a', 'B','b')
        self.box.current(0)
        self.box.grid(column=1, row=1)    
    def salir(self):
        print"Adios!"
        ser.close()
        root.destroy()
        sys.exit()
    def dato_recibido(self):
        d_temp = ser.readline()
        variable2.set(d_temp)
        d_display=Text(master=root,height=1.25, width=16)
        d_display.grid(column=1, row=4)
        d_display.insert(INSERT,d_temp)
        print 'Recibiendo: ' + d_temp
    def dato_enviar(self):
        d_temp = str(variable.get())
        ser.write(d_temp)         
        print "Eviando..."+d_temp

    def disminuir_velocidad(self):
        global variable3
        variable3=variable3-1
        if variable3<0:
            variable3=0
        print variable3
        lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        ser.write(lista[variable3].encode())
        print lista[variable3]
    def aumentar_velocidad(self):
        global variable3
        variable3=variable3+1
        if variable3>25:
            variable3=25
        print variable3
        lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        ser.write(lista[variable3].encode())
        print lista[variable3]
  
variable3=0
root = Tkinter.Tk()
root.title("Proyecto Circuitos 3")
root.geometry('900x650')
app = App(root)
root.mainloop()

