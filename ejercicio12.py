# Ejercicio 12. Distancias entre dos puntos de la tierra.
# La superficie de la tierra es curva y la distancia entre grados
#de longitud varia con la latitud. Como resultado, encontrar 
#la distancia entre dos puntos de la superficie de la tierra
#es mas complicado que usar el teorema de pitagoras.

#Si (t1,g1) y (t2,g2) es la latitud y longitud de dos puntos 
#de la superficie de la tierra. La distancia entre esos puntos,
#atravez de la superficie de la tierra, en kilometros es:

#distancia = 6371.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))

#Cree un programa que le permita al usuario introducir la 
#latitud y longitud de dos puntos de la tierra en grados.
#Su programa debe deplegar la distancia entre esos puntos,

#en kilometros. Tenga en cuenta que las funciones trigonometricas 
#en Python trabajan en radianes, por lo que debe convertir el 
#valor introducido en grados a radianes antes de utilizar la 
#formula. El modulo math contiene el comando radians, que 
#cambia de grados a radianes.

import math
la1=float(input('latitud 1: '))
lo1=float(input('longitud 1: '))
la2=float(input('latitud 2: '))
lo2=float(input('longitud 2: '))

t1= float(math.radians(la1))
g1=float(math.radians(lo1))
t2=float(math.radians(la2))
g2=float(math.radians(lo2))

distancia = float (6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))

print('la distancia entre puntos es %.3f' %distancia, 'kilometros')




 

#import math as ecuaciones- asi se puede cambiar el nombre de la libreria
#import math
#from math import cos, sin
#from math import *
# MANERAS DE LLAMAR MATH


#  C:\Users\alejandro\Desktop\7\programacion>python
#Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import math
#>>> dir(math)
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

