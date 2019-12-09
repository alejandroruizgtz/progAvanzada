#Introduccion a la programacion GUI7
#    (Graphical User Interface)

#Hasta ahora hemos escrito  algunos programas que se ejecutan 
#en una linea de comando. Sin embargo un usuario promedio espera 
#interactuar de forma grafica con la computadora. En python existe
#un modulo que se llama "tkinter" que probee una serie de 
#librerias estandar para el manejo de graficos en la computadora.
#Este modulo permite generar graficos en cualquier tipo de 
#plataformay utilizan el manejo de clases y objetos utilizando 
# una forma de programacion llamada programacion orientada a 
# eventos en el que un evento se activa cuando el usuario hace 
# algo, por ejemplo cuando se da un click en un boton o cuando 
# se presiona cierta tecla.
#Estas aplicaciones siempre deben de escuchar los eventos y 
# responder en el caso de que ocurra algun evento.



#Tk permite crear una ventana, despues marster

from tkinter import Tk, Label, Button

class MiPrimeraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Una GUI sencilla")  #nombre de ventana

        self.label = Label(master, text = "Mi primera GUI")
        self.label.pack()

        self.boton_saludo = Button(master, text = "Saludo", command=self.saludar)
        self.boton_saludo.pack() # prac agruta como se cre

        self.boton_dias = Button(master, text = "Buenos dias", command=self.buenos)
        self.boton_dias.pack()


        self.boton_cerrar = Button(master, text="Cerrar", command=master.quit)
        self.boton_cerrar.pack()

    def saludar(self):
        print("saludo!")
    
    def buenos(self):
        print("Buenos dias!")

root = Tk()   #manda a llamar y se le llama widget
mi_gui = MiPrimeraGUI(root)

root.mainloop()
