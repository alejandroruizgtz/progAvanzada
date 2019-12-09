#class
#metodo del constructor
     #atributos
class Gelatina:
    def __init__(self, color, sabor):
        self.color = color 
        self.sabor = sabor

    #metodos
    def desplegar_info(self):
        print('Mi color es: ', self.color, 'y mi sabor es: ',self.sabor)

gelatina1 = Gelatina ('rojo','grosella')
gelatina2 = Gelatina ('verde', 'limon')
gelatina3 = Gelatina ('morado','uva')

gelatina1.desplegar_info()
gelatina2.desplegar_info()
gelatina3.desplegar_info()




