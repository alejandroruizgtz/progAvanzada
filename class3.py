#cree una clase llamada triangulo. Su metodo __init__() debe tener como 
#argumentos self, angulo1, angulo2, angulo3. Haga uso del 
#constructor para crear apropiadamente estos atributos.

#Cree un metodo llamado checar_angulos. El metodo debe regresar
# True si la suma de self.angulo1, self.angulo2 y self.angulo3
#es igual a 180, de otra forma debera regresar False.

#Cree un objeto llamado mitrianguloo y pasele como argumento 
#tres angulos que sumen 180, por ejemplo 90, 60,30.

#Imprima mitriangulo.checar_angulos() para comprobar que 
#la clase esta bien implementada. Se debera imprimir True.

class triangulo:
    def __init__(self, angulo1, angulo2, angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3

    #metodos
    def checar_angulo(self):
        suma = self.angulo1 + self.angulo2 + self.angulo3
        if suma == 180:
            print('true')
        else:
            print('false')
            

mitriangulo = triangulo (90, 60, 30)
mitriangulo2 = triangulo(15, 69,5)

mitriangulo.checar_angulo()
mitriangulo2.checar_angulo()