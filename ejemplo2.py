### control de flujo
#si un programa no fuera mas que una lista de ordenes a ejecutar de forma secuencial una por una, no tendria mucha utilidad. Las sentencias condicionales nos permiten comprovar condiciones y hacer que nuestro programa se comporte de una forma u otra, que ejecute un fragmento de codigou otro dependiendo de esta condicion.
#Aqui es donde cobran su importancia el tipo Booliano y los operadores logicas y relacionales 

#La forma mas simple de una sentencia condicional es un if (del ingles si). Segido de la condicion a evaluar, (:) y en la sigiente linea identado el codigo a ejecutar en caso de que se cumpla dicha condicion
#== comparacion



## Condicional if
password= input('escribir pasguor')
if password== 'te comere':
    print('te empacharas')

## La identacion del codigo se realiza con 4 espacios.


### Estructura if...else
#esta estructura permite añadir un comportamiento en caso de que la condicion no resulte cierta, por ejemplo 

password= input('escribir pasguor')
if password== 'te comere':
    print('te empacharas')
else: print('eres popis')


### Estructura condicional if...elif...elif...else
#el comando elif es la contraccion de else if, en español si no
#ejemplo: 
edad=int(input('cuantos años tienes'))

if edad > 0 and edad <2:
    print('eres bebe')
elif edad >= 2 and edad < 9:
    print ('eres niño')

elif edad >= 9  and edad < 15:
    print('adolescente tonto')

elif edad >= 15 and edad < 25:
    print('estupendo joven')
elif edad >= 25 and edad < 45:
    print('adulto aburrido')
    
elif edad >= 45 and edad < 60:
    print('mediana edad')
elif edad >= 60:
    print('abuelo')
else:         
    print('insertar edad valida')