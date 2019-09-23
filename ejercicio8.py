# ejercicio 8. cajas de cereal
# un vendedor de una pagina de abarrotes en linea vende dos tipos de cajas de cereal. CornFlakes de 750gr y trix de 500gr. Escriba un programa que lea el numero de cajas de CornFlakes y cajas de trix, cuyo  valor debe ser introducido por el usuario. despues su programa debe calcular y mostrar el total del peso(en kilogramos) del envio.

c=int(input('numero de cajas de CornFlakes '))
t=int(input('numero de caja Trix '))



print('pesa', ((c*750)+(t*500))/1000 , 'kilos')