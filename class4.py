#Cuenta
class Cuenta:
    def __init__(self, monto):
        self.monto = monto
    def depositar(self, cantidad):
        self.monto = self.monto + cantidad
        print('depositaste' , cantidad, 'tu saldo es:' , self.monto)
    def retirar(self, cantidad):
        self.monto = self.monto - cantidad
        print('retiraste' , cantidad, 'tu saldo es:' , self.monto)

cuenta_francisca = Cuenta(100)
cuenta_francisca.depositar(1000)
cuenta_francisca.retirar(400)

cuenta_jose = Cuenta(100)
cuenta_jose.retirar(100)
