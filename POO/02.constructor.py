##en el constructor de especifica el estado incial de los objetos 
##que instancien la clase
class Automovil():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enMarcha = False
    
    #este metodo no esta encapsulado y puede ser accedido
    #desde fuera de la clase
    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos
        
        if self.enMarcha:
            return "arranco!!!"
        else:
            return "seguimos detenidos"
    
    def estado(self):
        if self.enMarcha:
            return "el auto esta en marcha"
        else:
            return "el auto esta detenido"

miAuto = Automovil()

print(miAuto.ruedas)
print(miAuto.estado())
print(miAuto.arrancar(True))
print(miAuto.estado())

miAuto2 = Automovil()

print("")
print(miAuto2.ruedas)
print(miAuto2.estado())
print(miAuto2.arrancar(False))
print(miAuto2.estado())



