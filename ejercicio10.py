# Ejercicio 10. Aritmetica
# cree un programa que lea dos valores enteros, a y b, introducidos por el usuario.
# La suma de a y a.
# La diferencia cuando a es sustraido a b.
# El producti de a y b.
# El coeficiente cuando a divide a b.
#El residuo cuando a divide a b.
# El resultado de log(a).
# El resultado de a a laa potencia b.
# Tip: utilizar la libreria math.



from math import log
a = float(input('Inserta numero: '))
b = float(input('Inserta numero: '))
print('La suma es: ',           a+b)
print('La diferencia es: ',     a-b)
print('El producto es: ',       a*b)
print('El cociente es:',        a/b)
print('Potencia:',             a**b)
print('El residuo de:',       a % b)
print('Logaritmo',           log(a))