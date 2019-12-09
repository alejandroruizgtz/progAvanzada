
#escribir una clase llamada estudiante que obedesca el 
# sigueinte diagrama qrm

class Estudiante:
    def __init__(self, nombre, matricula, creditos):
        self.nombre = nombre
        self.matricula = matricula
        self.creditos = creditos

    def desplegar_info(self):
        print('El estudiante se llama: ', self.nombre, 'y tiene la matricula: ',self.matricula, 'y tiene' , self.creditos, 'aprobados' )

Estudiante1 = Estudiante ('ale','16090616','5')
Estudiante2 = Estudiante ('pepe','1605616','1')
Estudiante3 = Estudiante ('edi','16090556','6')
Estudiante4 = Estudiante ('ed','16090256','4')
Estudiante5 = Estudiante ('edd','1609766416','0')

Estudiante1.desplegar_info()
Estudiante2.desplegar_info()
Estudiante3.desplegar_info()
Estudiante4.desplegar_info()
Estudiante5.desplegar_info()