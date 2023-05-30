"""
@author: Brandon Grande
"""
#-----Librerias para el algoritmo Adaline-------------------------------------#
import math
import numpy 
#-----Funcion para generar una lista de numeros aleatorios--------------------#
def generarPesos(num):
    #-----Semilla de numeros aletorios----------------------------------------#
    numpy.random.seed(None)
    w=[]
    for i in range(num):
        #-----Inserta el numero aletorio en la lista--------------------------#
        w.append(2*numpy.random.random()-1)
    return w 
#-----Funcion para entrenar la neurona----------------------------------------#
def entrenamientoAdeline(listaPatrones, listaDx):
    #-----Se genera una lista con 25 pesos para la neurona--------------------#
    w=generarPesos(25) 
    #-----Declaracion de variables iniciales del algoritmo--------------------#
    error=[0,0,0,0,0,0,0,0,0,0]
    alfa=0.1
    y=0
    epsilon=0.1
    numpy.array(w)
    promedioError=1
    generacion=1
    #-----Mientras el promedio de errores sea mayor al epsilon----------------#
    while(promedioError>epsilon): 
        suma=0
        print('\nGeneracion:',generacion)
        iteracion=0
        #-----Para cada uno de los patrones de entrada------------------------#
        for i in range(10):
            y=0
            #-----Para cada uno de los valores de un patron de entrada--------#
            for j in range(25):
                y=y+(listaPatrones[i][j]*w[j])
            #-----Suma de los errores-----------------------------------------#
            suma=suma+pow((listaDx[i]-y),2)
            error[i]=(listaDx[i]-y)
            #-----Para cada uno de los pesos realiza actualizacion------------#
            for k in range(25):
                w[k]=w[k]+(alfa*error[i]*listaPatrones[i][k])
            print('\nIteracion:',iteracion)
            print('Valor esperado:\n',listaDx[i])
            print('Valor de salida (Y):\n',y)
            print('Error:\n',abs(error[i]))
            iteracion+=1
         #-----Promedio de la suma de errores---------------------------------#
        promedioError=math.sqrt(suma/10)
        generacion+=1
        print('\nPromedio de errores:\n',promedioError)
    print('\nValores finales de pesos (W):')
    for b in range(25):
        print('W'+str(b+1)+':',w[b])
        
    return w
#-----Obtener posible digito por medio de los pesos del entrenamiento---------#
def obtenerPosibleDigito(listaPatron,wEntrenamiento):
    y=0
    for i in range(25):
        y=y+(listaPatron[i]*wEntrenamiento[i])
    print('\nPredicion:',y)       
    return y
#-----Lista que tiene los patrones de entrada---------------------------------#
listaPatrones=[

 [0,1,1,1,0,
  0,1,0,1,0,
  0,1,0,1,0,
  0,1,0,1,0,
  0,1,1,1,0]
 ,
 [0,1,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  0,1,1,1,0]
 ,
 [0,1,1,1,0,
  0,0,0,1,0,
  0,1,1,1,0,
  0,1,0,0,0,
  0,1,1,1,0]
 ,

 [0,1,1,1,0,
  0,0,0,1,0,
  0,1,1,1,0,
  0,0,0,1,0,
  0,1,1,1,0]
 ,
 [0,1,0,1,0,
  0,1,0,1,0,
  0,1,1,1,0,
  0,0,0,1,0,
  0,0,0,1,0]
 ,
 [0,1,1,1,0,
  0,1,0,0,0,
  0,1,1,1,0,
  0,0,0,1,0,
  0,1,1,1,0]
 ,

 [0,1,1,1,0,
  0,1,0,0,0,
  0,1,1,1,0,
  0,1,0,1,0,
  0,1,1,1,0]
  ,
 [0,1,1,0,0,
  0,0,1,0,0,
  0,1,1,1,0,
  0,0,1,0,0,
  0,0,1,0,0]
 ,
 [0,1,1,1,0,
  0,1,0,1,0,
  0,1,1,1,0,
  0,1,0,1,0,
  0,1,1,1,0]
 ,
 [0,1,1,1,0,
  0,1,0,1,0,
  0,1,1,1,0,
  0,0,0,1,0,
  0,0,0,1,0]
]
#-----Lista que tiene los valores esperados-----------------------------------#
listaDx=[0,1,2,3,4,5,6,7,8,9]
#-----Lista con el patron ingresado-------------------------------------------#
listaPatronIngresado=[0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0]