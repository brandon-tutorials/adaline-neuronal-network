"""
@author: Brandon Grande |
Stephany Gama | 
Nereyda Garcia 
"""
#----Importacion de algoritmo Adaline--------------------#
import Adaline
 #-----Librerias para interfaz grafica----------------#
from sys import version_info
from functools import partial
from PIL import ImageTk, Image

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
#-----Modificar el valor del boton y cambiar color en la interfaz-------------#
def modificarEstadoDeBoton(boton,posicion):
    if(boton.cget('background')=='white'):
        Adaline.listaPatronIngresado[posicion]=1
        boton.configure({'background': 'black'})
    else:
        Adaline.listaPatronIngresado[posicion]=0
        boton.configure({'background': 'white'})
        
#-----Identificar el numero para mostrarlo como resultado en la interfaz------#
def identificarNumero(listaPatronIngresado,numeroLabel,raiz):
    digitoObtenido=round(Adaline.obtenerPosibleDigito(Adaline.listaPatronIngresado,listaPesosDeEntrenamiento))
    path=""
    
    if(digitoObtenido==0):
        path = "./Imagenes/numeroCero.png"
    elif(digitoObtenido==1):
        path = "./Imagenes/numeroUno.png"
    elif(digitoObtenido==2):
         path = './Imagenes/numeroDos.png'
    elif(digitoObtenido==3):
        path = './Imagenes/numeroTres.png'
    elif(digitoObtenido==4):
        path="./Imagenes/numeroCuatro.png"
    elif(digitoObtenido==5):
        path="./Imagenes/numeroCinco.png"
    elif(digitoObtenido==6):
        path="./Imagenes/numeroSeis.png"
    elif(digitoObtenido==7):
        path="./Imagenes/numeroSiete.png"
    elif(digitoObtenido==8):
         path="./Imagenes/numeroOcho.png"
    elif(digitoObtenido==9):
         path="./Imagenes/numeroNueve.png"
    else:
         path="./Imagenes/numeroDesconocido.png"
    #-----Actualizar imagen en la interfaz grafica----------------------------#
    img = ImageTk.PhotoImage(Image.open(path))
    numeroLabel.config(image=img)
    numeroLabel= tk.Label(raiz,image=img,width=230, height=215)
    numeroLabel.place(x=470,y=44)
    raiz.mainloop()
    
    
    
    
#-----Realizar el eltrenamiento de la neurona Adaline-------------------------#
listaPesosDeEntrenamiento=Adaline.entrenamientoAdeline(Adaline.listaPatrones,Adaline.listaDx)



 #-----Raiz de la interfaz grafica (Panel principal)--------------------------#
raiz = tk.Tk()
 #-----Botones del tablero de la interfaz grafica-----------------------------#
boton1=tk.Button(raiz,background='white', activebackground="white", text="", width=5, height=2)
boton1.place(x=50,y=50)
boton1['command'] =  partial(modificarEstadoDeBoton,boton1,0)

boton2=tk.Button(raiz,background='white',  activebackground="white", text="", width=5, height=2)
boton2.place(x=95,y=50)
boton2['command'] =  partial(modificarEstadoDeBoton,boton2,1)

boton3=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton3.place(x=140,y=50)
boton3['command'] =  partial(modificarEstadoDeBoton,boton3,2)

boton4=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton4.place(x=185,y=50)
boton4['command'] =  partial(modificarEstadoDeBoton,boton4,3)

boton5=tk.Button(raiz,background='white',  activebackground="white", text="", width=5, height=2)
boton5.place(x=230,y=50)
boton5['command'] =  partial(modificarEstadoDeBoton,boton5,4)

boton6=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton6.place(x=50,y=91)
boton6['command'] =  partial(modificarEstadoDeBoton,boton6,5)

boton7=tk.Button(raiz,background='white',  activebackground="white", text="", width=5, height=2)
boton7.place(x=95,y=91)
boton7['command'] =  partial(modificarEstadoDeBoton,boton7,6)

boton8=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton8.place(x=140,y=91)
boton8['command'] =  partial(modificarEstadoDeBoton,boton8,7)

boton9=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton9.place(x=185,y=91)
boton9['command'] =  partial(modificarEstadoDeBoton,boton9,8)

boton10=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton10.place(x=230,y=91)
boton10['command'] =  partial(modificarEstadoDeBoton,boton10,9)

boton11=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton11.place(x=50,y=132)
boton11['command'] =  partial(modificarEstadoDeBoton,boton11,10)

boton12=tk.Button(raiz, background='white', activebackground="white", text="", width=5, height=2)
boton12.place(x=95,y=132)
boton12['command'] =  partial(modificarEstadoDeBoton,boton12,11)

boton13=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton13.place(x=140,y=132)
boton13['command'] =  partial(modificarEstadoDeBoton,boton13,12)

boton14=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton14.place(x=185,y=132)
boton14['command'] =  partial(modificarEstadoDeBoton,boton14,13)

boton15=tk.Button(raiz,background='white',  activebackground="white", text="", width=5, height=2)
boton15.place(x=230,y=132)
boton15['command'] =  partial(modificarEstadoDeBoton,boton15,14)

boton16=tk.Button(raiz,background='white',  activebackground="white", text="", width=5, height=2)
boton16.place(x=50,y=173)
boton16['command'] =  partial(modificarEstadoDeBoton,boton16,15)

boton17=tk.Button(raiz, background='white', activebackground="white", text="", width=5, height=2)
boton17.place(x=95,y=173)
boton17['command'] =  partial(modificarEstadoDeBoton,boton17,16)

boton18=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton18.place(x=140,y=173)
boton18['command'] =  partial(modificarEstadoDeBoton,boton18,17)

boton19=tk.Button(raiz, background='white', activebackground="white", text="", width=5, height=2)
boton19.place(x=185,y=173)
boton19['command'] =  partial(modificarEstadoDeBoton,boton19,18)

boton20=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton20.place(x=230,y=173)
boton20['command'] =  partial(modificarEstadoDeBoton,boton20,19)

boton21=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton21.place(x=50,y=214)
boton21['command'] =  partial(modificarEstadoDeBoton,boton21,20)

boton22=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton22.place(x=95,y=214)
boton22['command'] =  partial(modificarEstadoDeBoton,boton22,21)

boton23=tk.Button(raiz, background='white', activebackground="white", text="", width=5, height=2)
boton23.place(x=140,y=214)
boton23['command'] =  partial(modificarEstadoDeBoton,boton23,22)

boton24=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton24.place(x=185,y=214)
boton24['command'] =  partial(modificarEstadoDeBoton,boton24,23)

boton25=tk.Button(raiz,background='white', activebackground="white",  text="", width=5, height=2)
boton25.place(x=230,y=214)
boton25['command'] =  partial(modificarEstadoDeBoton,boton25,24)

#-----Label donde se agrega la foto-------------------------------------------#
path="./Imagenes/fondoBlanco.png"
img = ImageTk.PhotoImage(Image.open(path))
numeroLabel= tk.Label(raiz,image=img,width=230, height=215)
numeroLabel.place(x=470,y=44)

#-----Boton para identificar el numero----------------------------------------#
botonIdentificar = tk.Button(raiz,background='white',  text="Identificar", activebackground="white",width=10,height=2)
botonIdentificar.place(x=345,y=130)
botonIdentificar['command'] =  partial(identificarNumero,Adaline.listaPatronIngresado,numeroLabel,raiz)

#-----Forma del la raiz (Panel principal)-------------------------------------#
raiz.title("Aplicacion para detectar numeros") 
raiz.geometry("753x300") 
raiz.resizable(False,False)
raiz.iconbitmap('iconoInterfaz.ico')
raiz.config(bg="#00a8f3")       
raiz.mainloop()