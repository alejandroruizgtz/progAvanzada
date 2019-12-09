#ciclo for
# un ciclo for es usadopara realizar integraciones sobre una secuencia
#(que puede ser una lista, un conjunto o una cadena de caracteres).
#con el cicloFOR se pueden ejecutar un conjunto de instruciiones,
#una para cada elemento de una lista o un conjunto, por ejemplo:

#frutas = ["manzana", "naranja", "uva"]
#for x in frutas:
#    print(x)


 
#for i in range(10):
#    print(i)


#for linea in open ('hola.txt'):
#    print(linea)




#prara graficar
#import numpy as np 
#import matplotlib.pyplot as plt

#x = np.arange(100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.show()


#import numpy as np 
#import matplotlib.pyplot as plt

#x = np.arange(100)
#y = np.sin(x)
#plt.scatter(x,y)
#plt.show()


import turtle
ventana = turtle.Screen()
ventana.bgcolor("green")
ventana.title("Mi ventana")

rafael = turtle.Turtle()
rafael.shape("turtle")
rafael.color("blue")
rafael.pensize(2)
rafael.speed(10000)
#rafael.pendown()
#rafael.forward(100)
#rafael.left(90)
#rafael.forward(100)
#rafael.left(90)
#rafael.forward(100)
#rafael.left(90)
#rafael.forward(100)
#rafael.left(90)
#i = 1
#rafael.pendown()


#while i < 5:
    #rafael.forward(i*100)
    #rafael.left(90)
    #rafael.forward(i*100)
    #rafael.left(90)
    #rafael.forward(i*100)
    #rafael.left(90)
    #rafael.forward(i*100)
    #rafael.left(90)
    #i = i + 1




i = 1
while i < 36:
    rafael.forward(50)
    rafael.left(90)
    rafael.forward(50)
    rafael.left(90)
    rafael.forward(50)
    rafael.left(90)
    rafael.forward(50)
    rafael.left(90)

    rafael.left(10)
    i = i + 1
  
ventana.mainloop()