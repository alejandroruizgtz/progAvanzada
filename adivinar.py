#hacer un programa que le permita a un usuario adivinar el 4
# numero que esta siendo generado aleatoriamente por la 
# computadora, la cual le dara 5 oportunidades para adivinar.
##En caso de que el usuario adivine el numero, se tiene que 
# imprimir un texto de felicitacion, en caso de que no lo 
# adivine tiene que mostrar un mensaje de seguir intentando.

import random

intentos = 0
numero = random.randint(1,6)
print('adivina  un numero del 1 al 6')

while intentos < 5:
    n = int(input('escribe numero'))
    intentos += 1

    if n < numero:
        print('tienes otra oportunidad')

    elif n > numero:
        print('otra oportunidad')

    else:
        break

if n == numero:
    print('felicidades')
if n != numero:
    print('se terminaron los intentos , el numero era ' (numero))