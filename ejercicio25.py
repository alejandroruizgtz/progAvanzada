# Ejercicio 25. Unidades de tiempo 1
#crear un programa que le pida al usuario la duracion en dias,
#horas, minutos y segundos. Calcualar y desplegar la cantidad
#total de segundos de duracion.



dias = float(input('cuantos dias: '))
horas = float(input('cuantas horas: '))
min = float(input('cuantos minutos: '))
seg = float(input('cuantos segundos: '))

c = float(min*60)
a = float(dias*86400)

b = float(horas*3600)



print('los segundos en total:', a+b+c+seg)
