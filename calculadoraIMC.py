
from tkinter import Tk, Label, Button, Entry

class MiPrimeraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")
        
        self.etiqueta_peso = Label(master, text="Peso:")
        self.etiqueta_peso.grid(row=0, column=0)

        self.caja_texto_peso = Entry(master)
        self.caja_texto_peso.grid(row=0, column=1)
        
        self.etiqueta_altura = Label(master, text="Altura:")
        self.etiqueta_altura.grid(row=1, column=0)

        self.caja_texto_altura = Entry(master)
        self.caja_texto_altura.grid(row=1, column=1)

        self.boton_calcular = Button(master, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=2, column=0)

        self.boton_cerrar = Button(master, text="Cerrar", command=master.quit)
        self.boton_cerrar.grid(row=2, column=1)

    def calcular(self):
        texto1 = self.caja_texto_peso.get()
        texto2 = self.caja_texto_altura.get()
        peso = float(texto1)
        altura = float(texto2)
        imc = peso/altura**2
        if imc < 16:
            print('tiene delgadez severa')
        elif imc >= 16 and imc < 17:
            print('tiene delgadez moderada')
        elif imc >= 17 and imc < 18.5:
            print('tiene delgades leve')
        elif imc >= 18.5 and imc < 25:
            print('tiene un imc normal')
        elif imc >= 25 and imc < 30:
            print('tiene preobesidad')
        elif imc >= 30 and imc < 35:
            print('tiene obesidad leve')
        elif imc >= 35 and imc < 40:
            print('tiene obesidad media')
        elif imc >= 40:
            print('tiene obesidad mordida')
        else:
            print('opcion invalida')

        print('su imc fue de', imc)

root = Tk()
mi_gui = MiPrimeraGUI(root)
root.mainloop()