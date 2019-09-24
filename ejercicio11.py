# Ejercicio 11. Fuel efficiency.
# Ejercicio 11. Eficiencia del combustible 
# En los Estados Unidos, la eficiencia del combustible para 
# vehículos normalmente se expresa en millas por galón (MPG).
# En México, la eficiencia del combustible normalmente se
# expresa en litros por cien kilómetros (L / 100km). 
# Usa tus habilidades de investigación para determinar cómo 
# convertir de MPG a L / 100km.  Luego, cree un programa que 
# lea un valor del uso en unidades estadounidenses y muestre
# la eficiencia de combustible equivalente en unidades 
# mexicanas.



mpg = float(input('Inserte combustible mpg: '))
print ('L/100km', ((mpg*1.609)/3.785))