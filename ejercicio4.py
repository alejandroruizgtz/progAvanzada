# crear programa que lea el largo y el ancho de un campo de cultivo, introducido por el usuario y despliegue el area del campo en acres
largo= float(input('cual es el largo en metros? '))
ancho= float(input('cual es el ancho en metros? '))
acres=float(0.000247105)
print('El area del campo es de', largo*ancho*acres, 'acres')
