#Cuenta
class Cuenta:
    def __init__(self, monto, usuario, no_cuenta):
        self.monto = monto
        self.usuario = usuario
        self.no_cuenta = no_cuenta
    
    def depositar(self, cantidad):
        self.monto = self.monto + cantidad
        print('depositaste' , cantidad, 'tu saldo es:' , self.monto)
    
    def retirar(self, cantidad):
        self.monto = self.monto - cantidad
        print('retiraste' , cantidad, 'tu saldo es:' , self.monto)
    
    def imprimirestado(self):
        print('banco de la ver')
        print('cliente', self.usuario)
        print('cuenta' , self.no_cuenta)
        print('saldo' , self.monto)


cuenta_francisca = Cuenta(100, 'perro cara', '21651323')
cuenta_francisca.depositar(1000)
cuenta_francisca.retirar(400)
cuenta_francisca.depositar(50)
cuenta_francisca.imprimirestado()


cuenta_jose = Cuenta(100,'cara perro', '4168348')
cuenta_jose.retirar(100)
cuenta_jose.imprimirestado()