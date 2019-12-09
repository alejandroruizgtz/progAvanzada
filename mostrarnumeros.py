# mostrar numeros


from tkinter import Tk, Label, Button

class Numeros:
    def __init__(self, master):
        self.master = master
        master.title("Mostrar Numeros")  #nombre de ventana

        self.label = Label(master, text = "Mostrar")
        self.label.pack()

        self.boton_saludo = Button(master, text = "mostrar", command=self.mostrar)
        self.boton_saludo.pack() # prac agruta como se cre
        
        self.boton_cerrar = Button(master, text="Cerrar", command=master.quit)
        self.boton_cerrar.pack()


   

    def mostrar(self):
        i = 1
        while i <= 100:
            print(i)
            i = i + 1
        print('fin del programa')

     

root = Tk()
mi_gui = Numeros(root)
root.mainloop()
