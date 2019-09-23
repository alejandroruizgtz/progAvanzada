# hacer un programa en el que el usuario introdusca el nombre de la comida que ordeno en un restaurante y su presio. despues el programa debe calcular el subtotal, el iba, y la propina de toda la cuenta. La salida del programa debe parecerse a un tiquet de restaurante. Use un iba del 16% y una propina del 15% del subtotal. Los valores numericos deben tener dos decimales.
# introdusca el nombre de la comida
# introdusca el valor de la comida:
#introdusca el nombre de la comida:
#introdusca el valor de la comida:
#introdusca el nombre de la comida:
#introdusca el valor de la comida:
#introdusca el nombre de la comida:
#introdusca el valor de la comida:
#introdusca el nombre de la comida:
#introdusca el valor de la comida:



#subtotal:
#iva:
#propina:

#total 



nombre1= input('Introdusca el nombre de la comida 1: ')
precio1= float(input('Introdusca el valor de la comida 1: '))
 
nombre2= input('Introdusca el nombre de la comida 2: ')
precio2= float(input('Introdusca el valor de la comida 2: '))

nombre3= input('Introdusca el nombre de la comida 3: ')
precio3= float(input('Introdusca el valor de la comida 3: '))

nombre4= input('Introdusca el nombre de la comida 4: ')
precio4= float(input('Introdusca el valor de la comida 4: '))

nombre5= input('Introdusca el nombre de la comida 5: ')
precio5= float(input('Introdusca el valor de la comida 5: '))

subtotal=float(precio1 + precio2 + precio3 + precio4 +precio5)
iva=float(0.16)
propina=float(0.15)

print('subtotal=',subtotal)
print('iva=', subtotal*iva)
print('propina=',subtotal*propina)

print('total=',subtotal+subtotal*iva+subtotal*propina)