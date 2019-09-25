#ESCRIBA UN PROGRAMA QUE DETERMINE COMO UN OBJETO VIAJA CUANDO
#GOLPEA EL PISO. El usuario insertara la informacion de la 
#altura desde donde el objeto se deja caer, en metros(m). 
#Dado que el objeto se deja caer desde el reposo (velocidad
#inicial Vd=m/s). Asumiendo que la aceleracion debido a 
#lagravedad es 9.81m/s´2 y usando lam formula Vf=(Vo´2 + 2gd)´2/3. 
#calcule la velocidad final Vf usando la velocidad inicial V0, 
#la aceleracion g, y la distancia d.


import math
d = float(input('altura en metros: ') )
g = 9.81
print('Vf:', math.sqrt(2*g*d) )